import pickle
from sklearn.metrics import normalized_mutual_info_score


def pickle_object(file, save_location):
    """"Pickle and save object to a given location"""
    with open(save_location, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)


def unpickle_object(file_location: object) -> object:
    """Load pickled object from a given location"""
    with open(file_location, 'rb') as handle:
        file = pickle.load(handle)
    return file


def NMI_score(partition_true: dict, partition_predicted: dict):
    """"Calculate the NMI score as defined in the sklearn, metric for clustering"""
    return normalized_mutual_info_score(list(partition_true.values()), list(partition_predicted.values()))