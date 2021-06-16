# [SoftRas](https://github.com/ShichenLiu/SoftRas)

## Install

```bash
conda activate torch
python - <<-EOF
import platform
import torch
print(f"Python : {platform.python_version()}")
print(f"PyTorch: {torch.__version__}")
print(f"  CUDA : {torch.version.cuda}")
EOF

Python : 3.8.10
PyTorch: 1.9.0
  CUDA : 11.1
```

```bash
git clone https://github.com/ShichenLiu/SoftRas.git
cd SoftRas
python setup.py install
```

<!--
cat <<-EOF > ~/.pydistutils.cfg
[easy_install]
index_url = http://mirrors.aliyun.com/pypi/simple
EOF

# ~/.config/pip/pip.conf
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
pip config set install.trusted-host mirrors.aliyun.com
-->

## Applications

```bash
snap install ogre-meshviewer
```

<!--
snap install blender

sudo apt install -y openctm-tools
ctmviewer data/obj/spot/spot_triangulated.obj
-->

### Rendering

Run:

```bash
CUDA_VISIBLE_DEVICES=0 python examples/demo_render.py
```

Compare:

```bash
ogre-meshviewer data/obj/spot/spot_triangulated.obj

ogre-meshviewer data/results/output_render/saved_spot.obj
```

### 3D Unsupervised Single-view Mesh Reconstruction

Download datasets:

```bash
bash examples/recon/download_dataset.sh
```

Train the model:

```bash
CUDA_VISIBLE_DEVICES=0 python examples/recon/train.py -eid recon
```

Test the model:

```bash
CUDA_VISIBLE_DEVICES=0 python examples/recon/test.py -eid recon \
    -d 'data/results/models/recon/checkpoint_0200000.pth.tar'
```

<!--
Download models (to `data/models/recon`):

- SoftRas trained with silhouettes supervision (62+ IoU): [google drive](https://drive.google.com/file/d/1GlZJVih5BMGp026mpxK2scWJXqT94VUx/view?usp=sharing)
- SoftRas trained with shading supervision (64+ IoU, test with `--shading-model` arg): [google drive](https://drive.google.com/file/d/1r63AKNn3ecMho6RFE7gFefRv78Pmbe5h/view?usp=sharing)
- SoftRas reconstructed meshes with color (random sampled): [google drive](https://drive.google.com/file/d/1gnSshn0k9JpVpoSTWIQoV2QFAlin3AUK/view?usp=sharing)

CUDA_VISIBLE_DEVICES=0 python examples/recon/test.py -eid recon \
    -d 'data/models/recon/softras_checkpoint_model.tar'

CUDA_VISIBLE_DEVICES=0 python examples/recon/test.py -eid recon --shading-model \
    -d 'data/models/recon/softras_shading_checkpoint.pth.tar'
-->

## See also

- [Jrender](https://github.com/Jittor/jrender) - [Jittor](https://cg.cs.tsinghua.edu.cn/jittor/)
  - [JRender 解读](https://zhuanlan.zhihu.com/p/336364959)
  - [3D Recon](https://github.com/Jittor/shapenet-reconstruction-jittor)
