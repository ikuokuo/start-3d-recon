import argparse
import os

import imageio
import numpy as np
import torch
import tqdm

import soft_renderer.functional as srf
from softras import models, models_large
from softras.utils import img_cvt


## arguments

parser = argparse.ArgumentParser()
# model
parser.add_argument('-s', '--softras-dir', type=str, required=True)
parser.add_argument('-d', '--model-path', type=str, required=True)
parser.add_argument('-is', '--image-size', type=int, default=64)
parser.add_argument('-sv', '--sigma-val', type=float, default=0.01)
parser.add_argument('--shading-model', action='store_true', help='test shading model')
# image
parser.add_argument('-img', '--image-path', type=str, default=None)
parser.add_argument('-imgs', '--images-path', type=str, default=None)
parser.add_argument('-o', '--output-dir', type=str, default='_output')
args = parser.parse_args()

## setup model & optimizer

print(f'load: {args.model_path}')

obj_path=f'{args.softras_dir}/data/obj/sphere/sphere_642.obj'
if args.shading_model:
  model = models_large.Model(obj_path, args=args)
else:
  model = models.Model(obj_path, args=args)

model = model.cuda()

state_dicts = torch.load(args.model_path)
# import ipdb; ipdb.set_trace()
model.load_state_dict(state_dicts['model'], strict=True)
model.eval()
# print(model)

## mesh recon

def mesh_recon(x):
  if x.ndim == 4:
    pass
  elif x.ndim == 3:
    x = x[np.newaxis, :]
  else:
    raise ValueError('X must be 3/4 dims: CHW/BCHW.')

  assert x.shape[1] == 4, 'C must be 4: rgba.'
  # print(f'  {x.shape}')

  x = np.ascontiguousarray(x)
  x = x.astype('float32') / 255.
  x = torch.autograd.Variable(torch.from_numpy(x)).cuda()
  _, vertices, faces = model(x, task='test')

  return x, vertices, faces

## read images

if args.image_path and os.path.exists(args.image_path):
  print(f'read: {args.image_path}')
  image = imageio.imread(args.image_path)
  x = image.transpose(2, 0, 1) # HWC > CHW

  _, vertices, faces = mesh_recon(x)

  obj_path = os.path.splitext(args.image_path)[0] + '.obj'
  print(f'save: {obj_path}')
  srf.save_obj(obj_path, vertices[0], faces[0])

if args.images_path and os.path.exists(args.images_path):
  class_ids_map = {
    '02691156': 'Airplane',
    '02828884': 'Bench',
    '02933112': 'Cabinet',
    '02958343': 'Car',
    '03001627': 'Chair',
    '03211117': 'Display',
    '03636649': 'Lamp',
    '03691459': 'Loudspeaker',
    '04090263': 'Rifle',
    '04256520': 'Sofa',
    '04379243': 'Table',
    '04401088': 'Telephone',
    '04530566': 'Watercraft',
  }
  class_id = os.path.basename(args.images_path)[:8]
  class_name = class_ids_map[class_id]
  print(f'read: {args.images_path}, {class_name}')

  images = list(np.load(args.images_path).items())[0][1]
  images = images.reshape((-1, 4, 64, 64))

  output_dir = os.path.join(args.output_dir, class_name)
  os.makedirs(output_dir, exist_ok=True)
  print(f'save: {output_dir}/')

  images_n = images.shape[0]
  batch_size = 100
  print(f' num: {images_n}')

  for i in tqdm.tqdm(range((images_n-1) // batch_size + 1)):
    x = images[i*batch_size:(i+1)*batch_size]

    x, vertices, faces = mesh_recon(x)

    for j in range(vertices.size(0)):
      k = i*batch_size + j
      # save obj
      srf.save_obj(f'{output_dir}/{k:06d}.obj', vertices[j], faces[j])
      # save img RGBA
      imageio.imsave(f'{output_dir}/{k:06d}.png', img_cvt(x[j]))
