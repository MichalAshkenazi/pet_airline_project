import pickle
import os
import pandas as pd

if __name__ == '__main__':
    dir = "/Users/michal.ashkenazi/git_rep/pet/airline/raw"
    dir2 = "/Users/michal.ashkenazi/git_rep/pet/airline"
    paths = [
        "dev",
        "test",
        "train",
        "unlabeled"
    ]

    for file_path in paths:
        with open(os.path.join(dir, file_path), 'rb') as f:
            if file_path!="unlabeled":
                (train, train_labels) = pickle.load(f)
                df = pd.DataFrame(list(zip([a+1 for a in train_labels], train)))
                # df["2"] = -1
                # df[0] = df[0].map({0:1, 1:2})
                # df[2] =-1c
                df.to_csv(os.path.join(dir2, f"{file_path}.csv"), index=False)
                print(file_path)
            else:
                train = pickle.load(f)
                df = pd.DataFrame(train, columns=[1])
                df["2"] = "unlabeled"
                df.to_csv(os.path.join(dir2, f"{file_path}.csv"), index=False)
