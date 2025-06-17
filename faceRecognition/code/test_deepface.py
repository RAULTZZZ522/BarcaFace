from deepface import DeepFace # type: ignore
import os
import cv2

def test_face_comparison():
    # 获取测试图片的路径
    test_dir = os.path.join('facerecognition', 'data', 'test')
    
    # 检查test目录是否存在
    if not os.path.exists(test_dir):
        print(f"错误：{test_dir} 目录不存在")
        return
        
    # 获取test目录下的所有图片
    image_files = [f for f in os.listdir(test_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if len(image_files) < 2:
        print("错误：test目录中需要至少两张图片")
        return
        
    # 选择前两张图片进行比较
    img1_path = os.path.join(test_dir, image_files[0])
    img2_path = os.path.join(test_dir, image_files[1])
    
    print(f"正在比较图片：\n{img1_path}\n{img2_path}")
    
    # 检查图片文件是否存在
    if not os.path.exists(img1_path):
        print(f"错误：找不到图片 {img1_path}")
        return
    if not os.path.exists(img2_path):
        print(f"错误：找不到图片 {img2_path}")
        return
        
    # 尝试读取图片
    try:
        img1 = cv2.imread(img1_path)
        if img1 is None:
            print(f"错误：无法读取图片 {img1_path}")
            return
        print(f"成功读取图片1，尺寸：{img1.shape}")
    except Exception as e:
        print(f"读取图片1时出错: {str(e)}")
        return
        
    try:
        img2 = cv2.imread(img2_path)
        if img2 is None:
            print(f"错误：无法读取图片 {img2_path}")
            return
        print(f"成功读取图片2，尺寸：{img2.shape}")
    except Exception as e:
        print(f"读取图片2时出错: {str(e)}")
        return
    
    try:
        # 使用DeepFace进行人脸验证
        result = DeepFace.verify(img1_path, img2_path)
        
        # 计算相似度百分比（将distance转换为相似度）
        similarity = (1 - result['distance']) * 100
        
        print("\n比较结果：")
        print(f"是否匹配: {result['verified']}")
        print(f"距离值: {result['distance']:.4f}")
        print(f"相似度: {similarity:.2f}%")
        print(f"阈值: {result['threshold']}")
        print(f"模型: {result['model']}")
        print(f"检测器: {result['detector_backend']}")
        
    except Exception as e:
        print(f"人脸比较时出错: {str(e)}")
        print("请确保图片中包含清晰的人脸，并且图片格式正确")

if __name__ == "__main__":
    test_face_comparison() 