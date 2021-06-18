# Start 3D Reconstruction

## 实践

### 可微渲染

可微渲染通过计算渲染过程的导数，使得从单张图片学习三维结构逐渐成为现实。可微渲染目前被广泛地应用于三维重建，特别是人体重建、人脸重建和三维属性估计等应用中。

了解：

- [什么是可微分渲染（differentiable rendering）](https://www.zhihu.com/question/364770565/answer/1266067986)

技术：

- [SoftRas](docs/softras.md)

## 参考

技术：

- AR
  - [ARKit - Apple](https://developer.apple.com/cn/augmented-reality/arkit/)
    - 2021 [Create 3D models with Object Capture](https://developer.apple.com/videos/play/wwdc2021/10076/) ⭐
      - Apps: [Wayfair](https://apps.apple.com/us/app/wayfair-shop-all-things-home/id836767708), [Etsy](https://apps.apple.com/us/app/etsy-custom-creative-goods/id477128284)
      - Article: [Apple’s RealityKit 2 allows developers to create 3D models for AR using iPhone photos](https://techcrunch.com/2021/06/08/apples-realitykit-2-allows-developers-to-create-3d-models-for-ar-using-iphone-photos/)
  - [ARCore - Google](https://developers.google.com/ar/)
- 单目深度估计
  - [Monocular Depth Estimation](https://paperswithcode.com/task/monocular-depth-estimation)
    - 2021 BoostingMonocularDepth: [Paper](https://arxiv.org/abs/2105.14021), [Code](https://github.com/compphoto/BoostingMonocularDepth)
    - 2020 AdaBins: [Paper](https://arxiv.org/abs/2011.14141), [Code](https://github.com/shariqfarooq123/AdaBins)
- 稠密视觉 SLAM
  - 2019 RTAB-Map: [Site](http://introlab.github.io/rtabmap/), [Code](https://github.com/introlab/rtabmap), [App](https://apps.apple.com/ca/app/rtab-map-3d-lidar-scanner/id1564774365) ⭐
  - 2016 DSO: [Site](https://vision.in.tum.de/research/vslam/dso), [Code](https://github.com/JakobEngel/dso)
- 三维重建
  - [三维重建 - 知乎](https://www.zhihu.com/column/c_1278034190307295232)
    - [三维重建有哪些实用算法？](https://www.zhihu.com/question/29885222)
    - [基于深度学习的视觉三维重建研究总结](https://zhuanlan.zhihu.com/p/79628068)
    - [目前有没有双目三维重建开源项目？](https://www.zhihu.com/question/419497403/answer/1459111592) ⭐
  - [Awesome 3D reconstruction list](https://github.com/openMVG/awesome_3DReconstruction_list) ⭐
  - [SLAM-based 3D Reconstruction](https://www.google.com.hk/search?q=slam-based+3D+reconstruction)
    - 2020 NodeSLAM: [Paper](https://arxiv.org/abs/2004.04485v2), [Video](https://www.youtube.com/watch?v=zPzMtXU-0JE)
    - 2019 MID-Fusion: [Paper](https://arxiv.org/abs/1812.07976), [Video](https://www.youtube.com/watch?v=gturboNl9gg)
    - 2018 Fusion++: [Paper](https://arxiv.org/abs/1808.08378), [Video](https://www.youtube.com/watch?v=2luKNC03x4k)
  - [3D Object Reconstruction from 2D Image](https://paperswithcode.com/task/3d-object-reconstruction)
    - 2020 Pix2Vox++: [Paper](https://arxiv.org/abs/2006.12250), [Code](https://gitlab.com/hzxie/Pix2Vox)
    - 2019 SoftRas: [Paper](https://arxiv.org/abs/1904.01786), [Code](https://github.com/ShichenLiu/SoftRas)
  - [PyTorch3D](https://pytorch3d.org/)

<!--
- [Computer Vision and Pattern Recognition](https://arxiv.org/list/cs.CV/recent)
-->

产品：

- [Mobile3DRecon - 商汤](https://zhuanlan.zhihu.com/p/340463853)
- [GrokNet, Rotating View - Facebook](https://ai.facebook.com/blog/powered-by-ai-advancing-product-understanding-and-building-new-shopping-experiences/)
- [众趣科技: 3D Pro 扫描仪](http://www.3dnest.cn/page/products/product_scaner1.html)
- [贝壳如视: VR扫描设备](http://www.realsee.com/website/product/hardware)
