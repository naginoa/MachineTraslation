# MachineTraslation in THU

My graduation project of Machine Translation from TsingHua Univercity.

## Changelog
All notable changes to this project will be documented in this file.

### Changed
- Update and improvement


## [0.1.0] - 2019-03-04
### Added
- Add the function of extracting ppt.
- baseline：bleualign.
- pipeline were done.

### Changed
-

### Removed
- 

## [0.0.4] - 2018-12-7
### Added
- add two python scripts to count the score and generate test.ref

### Changed
- Use our generated vocabulary through the our selfves datasets because the chinese Corpus need to Participle. While english sentences just need to split by space and in chinese it doesn't work well. It can be seen as bellows。
```
def sentence_to_token_ids(sentence, vocabulary, max_sequence_length):
    """Convert a string to a list of integers representing token-ids."""
    words = sentence.strip().split()
    if len(words) > max_sequence_length:
        words = words[:max_sequence_length]
    return [vocabulary.get(w, UNK_ID) for w in words]
```
跑模型中英文效果不好的原因有代码在的词库获取就是通过简单的空格，英语法语可以但是中文不行，所以用我们自己分好词的词库，并改代码逻辑！
 
### performance
- 训实验室的数据很大，英文好烦下次再说吧
```
Training: Loss = 0.010259, Accuracy = 0.9734, Precision = 0.9990, Recall = 0.8414, F1 = 0.9135
Validing:  Loss = 0.501839, Accuracy = 0.9696, Precision = 0.0044, Recall = 0.1738, F1 = 0.0085
```
train上的表现比较好，valid上loss太大,accuracy和precision不匹	配,recall也过低。研究论文和代码发现，论文的分词是取空格隔开这样，加	标点符号抽取，这样做西语确实可以分词但是中文不行。因此选用实验室的	词表，并修改代码逻辑。
- 分词用1000行pair跑一下结果如下：
```
Training: Loss = 0.137343, Accuracy = 0.8336, Precision = 1.0000, Recall = 0.0040, F1 = 0.0079
Validing:  Loss = 0.192807, Accuracy = 0.9981, Precision = 0.0000, Recall = 0.0000, F1 = 0.0000
```
明显看到loss降下来了。Precision和recall是因为负样本太多，判正的正	样本极少但不为0.
Test:
```
Evaluation metrics at decision threshold = 0.0652
Precision = 31.58, Recall = 10.81, F1 = 35.39
```
判断label为1的概率score分布：
```
the numbers of score_count <= 0.01 is 8
the numbers of score_count > 0.01 and <= 0.1 is 1
the numbers of score_count > 0.1 and <= 0.3 is 4
the numbers of score_count > 0.3 and <= 0.5 is 3
the numbers of score_count > 0.5 and <= 0.7 is 2
the numbers of score_count > 0.7 is 1
```

- 接下来找其他参数的原因。
目前训练集是1000，接下来扩大数据集看看概率分布会不会有改善。

## [0.0.3] - 2018-12-6
- I review the paper and code very very carefully.

## [0.0.2] - 2018-12-5
### Added
- train data. This model has 15 epoch, batch_size is 128, each epoch need about 2 hours(training on THU server with TF-GPU-1.12, CUDA9 and GTX1080).
- use [byobu](http://byobu.co/) to do things on Linux.

### Changed
- change dataset from HIT to PKU that we used to get.The data from PKU are the real medical data. The size of new dataset become nearly about 80M.

### Removed
- 

## [0.0.1] - 2018-12-4
### Added
- find papers about sentence alignment.
- choose the first paper to implement.
[Extracting Parallel Sentences with Bidirectional Recurrent Neural Networks to Improve Machine Translation](https://arxiv.org/abs/1806.05559)
- choose the dataset of HIT as aligned parallel corpus.[HIT_CIR_LTP_Sharing](http://ir.hit.edu.cn/demo/ltp/Sharing_Plan.htm)
- BiRNN [code](https://github.com/naginoasukara/THU_MT/tree/master/sentence%20alignment/BiRNN%20for%20SA) here.

### Changed
-

### Removed
- 
