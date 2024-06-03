import os


def get_file_list(path):
    file_list = []
    ori_dir_list = [path]
    for ori_path in ori_dir_list:
        for path in os.listdir(ori_path):
            path=os.path.join(ori_path,path)
            if os.path.isdir(path):
                ori_dir_list.append(path)
            else:
                if path.split(".")[-1] == "7z":
                    file_list.append(path)
    return file_list


