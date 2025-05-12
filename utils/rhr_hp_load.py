import yaml
from models.rhrnetdir.Arg_Parser import Recursive_Parse
  
def load_rnn_hp():
    return Recursive_Parse(yaml.load(
    open('models/rhrnetdir/rhrnet_hyperparameters.yaml', encoding='utf-8'),
    Loader=yaml.Loader
    ))
