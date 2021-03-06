import os.path
import json

from tracking import *

animal_model_to_str = { tracking.Animal.Configuration.model_normal : "normal",
                        tracking.Animal.Configuration.model_with_drive : "with_drive" }
str_to_animal_model = dict([[v,k] for k,v in animal_model_to_str.items()])        

def load_tracking_config(file_name):    
    config = tracking.Tracking.Configuration()
    
    if not os.path.isfile(file_name):
        save_tracking_config(config, file_name)
    else:
        data_file = open(file_name)
        data = json.load(data_file)    
        config.skeletonization_res_width = data["skeletonization_res_width"]
        config.skeletonization_res_height = data["skeletonization_res_height"]
        config.vertebra_length = data["vertebra_length"]
        config.scale = data["scale"]
        
    return config


def save_tracking_config(config, file_name):
    file = open(file_name, 'w') 
    json.dump({ 'skeletonization_res_width': config.skeletonization_res_width,
                'skeletonization_res_height': config.skeletonization_res_height,
                'vertebra_length': config.vertebra_length,
                'scale': config.scale }, file, indent = 4)

def load_animal_config(file_name):    
    config = tracking.Animal.Configuration()
    
    if not os.path.isfile(file_name):
        save_animal_config(config, file_name)
    else:
        data_file = open(file_name)
        data = json.load(data_file) 

        config.back_min_value_coeff = data["back_min_value_coeff"]
        config.front_min_value_coeff = data["front_min_value_coeff"]
        config.max_body_length = data["max_body_length"]
        config.max_body_width = data["max_body_width"]
        config.min_body_width = data["min_body_width"]
        config.model = str_to_animal_model[data["model"]]
        
    return config


def save_animal_config(config, file_name):
    file = open(file_name, 'w') 
    json.dump({ 'back_min_value_coeff': config.back_min_value_coeff,
                'front_min_value_coeff': config.front_min_value_coeff,
                'max_body_length': config.max_body_length,
                'model': animal_model_to_str[config.model],
                'max_body_width': config.max_body_width,
                'min_body_width': config.min_body_width }, file, indent = 4)
                
                