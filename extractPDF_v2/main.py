import os
from get_pairs import gen_pairs_folder
from extract_PPT import ppt2txt
from batch_split import batch_split_files
from batch_google_trans import batch_trans
from batch_segmentation import batch_segment
from final_remove_space import remove_space


oripath = 'D:/v2_extract/oridata/'
pairspath = 'D:/v2_extract/pairs/'
textpath = 'D:/v2_extract/text/'
splitpath = 'D:/v2_extract/split/'
transpath = 'D:/v2_extract/translation/'
segpath = 'D:/v2_extract/segmentation/'
bleupath = 'D:/v2_extract/result_bleu/'
resultpath = 'D:/v2_extract/final_result/'


if __name__ == "__main__":
    # 对文件进行第一次配对并改名
    gen_pairs_folder(oripath, pairspath)
    # 抽取PPT
    dele_flist = ppt2txt(pairspath, textpath)
    for df in dele_flist:
        os.remove(df)

    # 此处需手动进行批量操作 使用金山PDF和doc2docx工具进行批量转换 到text文件下

    # 进行分句
    batch_split_files(textpath, splitpath)
    # 进行翻译 test_proxy.py 可以测试代理IP是否可用
    batch_trans(splitpath, transpath)
    # 对翻译和译稿进行分句，并直接将原本en也拷贝进入segpath中
    batch_segment(splitpath, transpath, segpath)

    # 此处直接将segmentation文件打包 拷贝入 linux中进行bleualign
    # 拷贝到 /home/renxy/mt/sentence_alignment/Bleualign-master/batch_full_set
    # 批量对齐脚本为 /home/renxy/mt/sentence_alignment/Bleualign-master/batch_align.py
    # 对齐后将 .aligned 的结果拷入blue_path 路径即可

    # 对结构进行一定过滤，已经生成结果
    remove_space(bleupath, resultpath)

    # 若要合并一个文件，则单独运行一下result_merge.py 即可