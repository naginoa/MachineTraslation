# MachineTraslation in THU

My graduation project of Machine Translation from TsingHua Univercity.

## Changelog
All notable changes to this project will be documented in this file.

### Changed
- Update and improvement

## [0.0.4] - 2018-12-7
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
- 

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
