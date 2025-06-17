import os
from PIL import Image
import glob

def convert_images():
    # 获取data目录下的所有文件夹
    data_dir = os.path.join('facerecognition/data')
    if not os.path.exists(data_dir):
        print(f"错误：{data_dir} 目录不存在")
        return

    # 遍历data目录下的所有文件夹
    for folder_name in os.listdir(data_dir):
        folder_path = os.path.join(data_dir, folder_name)
        
        # 确保是文件夹
        if not os.path.isdir(folder_path):
            continue
            
        print(f"处理文件夹: {folder_name}")
        
        # 获取文件夹中所有图片文件
        image_files = []
        for ext in ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif'):
            image_files.extend(glob.glob(os.path.join(folder_path, ext)))
        
        # 处理每个图片
        for index, image_path in enumerate(image_files, 1):
            try:
                # 打开图片
                with Image.open(image_path) as img:
                    # 创建新的文件名
                    new_filename = f"{folder_name}_{index}.jpg"
                    new_path = os.path.join(folder_path, new_filename)
                    
                    # 如果图片不是RGB模式，转换为RGB
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # 保存为jpg格式
                    img.save(new_path, 'JPEG')
                    
                    # 如果原文件不是新文件，则删除原文件
                    if image_path != new_path:
                        os.remove(image_path)
                        
                print(f"已转换: {os.path.basename(image_path)} -> {new_filename}")
                
            except Exception as e:
                print(f"处理图片 {image_path} 时出错: {str(e)}")

if __name__ == "__main__":
    convert_images() 