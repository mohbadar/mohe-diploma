import json


def load_json(jsonstr):
    return json.loads(jsonstr)

def load_all_steps(jsonobj):
    if jsonobj:
        return jsonobj["steps"]
    return None

def load_init_step(jsonobj):
    if jsonobj:
        return jsonobj["steps"][0]
    return None

def load_step_by_name(stepname,steps):
    for step in steps:
        if step['name'] == stepname:
            return step
    return None

def load_step_by_tostep(tostep,transition):
    for step in steps:
        if step['tostep'] == tostep:
            return step
    return None

def load_step_transitions(step):
    if step:
        return step['transitions']
    return None

def load_step_required_authorties(step):
    if step:
        return step['requiredAuthorities']
    return None

def has_authority(step , authorties):
    
    required_authorities = load_step_required_authorties(step)
    result =  any(elem in required_authorities  for elem in authorties)
    return result

def load_authorized_next_transition(instance_current_stepname,steps, authorities):
    if instance_current_stepname == None:
        return load_init_step(jsonobj)
    else:
        currentstep = load_step_by_name(instance_current_stepname, steps)
        step_transitions = load_step_transitions(currentstep)
        authorized_transitions = []
        
        for transition in step_transitions:
            tostep = transition['toStep']
#             print(tostep)
            step  = load_step_by_name(tostep,steps)
            
            authorized = has_authority(step,authorities)
            
            if authorized :
                authorized_transitions.append(step)
                
        return authorized_transitions

