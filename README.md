# tweets-clustering

## Examples

To run the examples just do `python <file-name>`

## Models

To use the Tweet model import the file by doing `from models.tweet import Tweet`

See [Orator ORM](https://orator-orm.com/docs/0.9/orm.html#introduction) to see more examples on how to use the models

## Training

For training a word2vec model use

```python
python train_word2vec.py -i <input-path> -o <output-path>
```

If the input path is a folder it will read all files inside, if it is a file it will only read that file. When the training process is ready it will save the model to the specified <output-file>.
