import os

import deepdanbooru as dd


def evaluate(project_path, target_path, threshold):
    if not os.path.exists(target_path):
        raise Exception(f'Target path {target_path} is not exists.')

    if os.path.isfile(target_path):
        taget_image_paths = [target_path]


    else:
        patterns = [
            '*.[Pp][Nn][Gg]',
            '*.[Jj][Pp][Gg]',
            '*.[Jj][Pp][Ee][Gg]',
            '*.[Gg][Ii][Ff]'
        ]

        taget_image_paths = dd.io.get_file_paths_in_directory(
            target_path, patterns)

        taget_image_paths = dd.extra.natural_sorted(taget_image_paths)

    project_context, model, tags = dd.project.load_project(project_path)

    width = project_context['image_width']
    height = project_context['image_height']

    result = {}
    coun=0
    for image_path in taget_image_paths:
        coun+=1
        image_name = image_path.split('\\')[-1]
        print('正在分析{0}中……  剩余：{1}'.format(image_path.replace('\\','/'),len(taget_image_paths)-coun))
        try:
            image = dd.data.load_image_for_evaluate(
                image_path, width=width, height=height)

            image_shape = image.shape
            image = image.reshape(
                (1, image_shape[0], image_shape[1], image_shape[2]))
            y = model.predict(image)[0]

            tag_list = []

            for i, tag in enumerate(tags):
                if y[i] < threshold:
                    continue
                tag_list.append(tag)

            result[image_path] = tag_list
        except Exception:
            print('{0}无法识别'.format(image_path))
            result[image_path] = '000000'
    return result
