from ....persistence.judgement import getjudgementtracker
from ....persistence.ideas import getideaslist
from ....persistence.ideacategories import getideacategories

import json

def process_score(request:dict)->dict:
    
    '''
       Below would be the structure for judgement tracking against every single idea. 
       This structure can be further extended to include the list of viewer comments as well.
       
       judgement_tracking: { 
                              "0": [ _total: {"idea_pitch":6,}, _judge1: { "idea_pitch" : 7, }, _judge2 { idea_pitch: 5}, ],
                              "1": [ ],
                              "2": {},
                              "3": {}
                           }
                           
    '''
    
    '''

       This structure would be for freezing of the judgement against the ideas. 
       Basically, in this, key would be judge_id and and value would be dictionary of ideas key value pair as _ideaid:boolean
       True indicates, judgement against that idea has been frozen for further change.
       
       judgement_freeze_flags: {
                                 "_judgetoken":[{"0":true},{"1":false},..]
                               } 
    '''
    
    # 1. first get the idea id for which judgement provision is requested for
    # 2. fetch the category to which idea belongs
    # 3. fetch the criteria of judgement category to which it belongs
    # 4. Validate the input values against the prescribed judgement criteria. If the validation fails, send across the error
    #    so that user again feeds in the correct values
    
    # 1. Validate that the given scores are within the scale of 1-10 and if those are
    total = 0
    requested_fields =  request.keys()
    transformed_scores_to_int = {}
    
    if ('idea_pitch' not in requested_fields):
        return {"error":"mandatory field idea_pitch is missing"}
    else:
        transformed_scores_to_int['idea_pitch'] = int(request['idea_pitch'])
        total += transformed_scores_to_int['idea_pitch']
        
    while True:
        if('efficiency_value' in requested_fields):
            break
        elif('feature_value' in requested_fields):
            break
        elif('business_value' in requested_fields):
            break
        else:
            return {"error":"mandatory field efficiency_value/feature_value/business_value is missing"}

    if('efficiency_value' in requested_fields): 
        transformed_scores_to_int['efficiency_value'] = int(request['efficiency_value'])
        total += transformed_scores_to_int['efficiency_value'] 
    elif ('feature_value' in requested_fields):
        transformed_scores_to_int['feature_value'] = int(request['feature_value'])
        total += transformed_scores_to_int['feature_value']
    elif ('business_value' in requested_fields):
        transformed_scores_to_int['business_value'] = int(request['business_value'])
        total += transformed_scores_to_int['business_value']
            
    if ('future_scope' not in requested_fields):
        return {"error":"mandatory field future_scope is missing"}
    else:
        transformed_scores_to_int['future_scope'] = int(request['future_scope'])
        total += transformed_scores_to_int['future_scope']
        
    if ('working_model' not in requested_fields):
        return {"error":"mandatory field working_model is missing"}
    else:
        transformed_scores_to_int['working_model'] = int(request['working_model'])
        total += transformed_scores_to_int['working_model']
        
    if ('presentation' not in requested_fields):
        return {"error":"mandatory field presentation is missing"}
    else:
        transformed_scores_to_int['presentation'] = int(request['presentation'])
        total += transformed_scores_to_int['presentation']

      
    # 2. get the idea id from request for which judgement provision is requested for
    if("id" not in request.keys()):
        return {"error":"id field is missing in the request"}
    idea_id = request["id"]

    # 3. get the idea category from idea_list using the id
    idea_list = getideaslist.fetch_idea_list()
    required_idea = None
    idea_category = None

    for each_idea in idea_list:
        if(each_idea['id'] == int(idea_id)):
            required_idea = each_idea
            
    if required_idea is None:
        return {"error":"Could not fetch the idea details corresponding to the id "+idea_id }
    else:
        idea_category = required_idea['category']
    
    # 4. get the criteria of judgement category to which it belongs
    judgement_criteria = None
    idea_categories = getideacategories.get_idea_categories()
    for category in idea_categories.keys():
        if (idea_category == category):
            # We got our judgement criteria
            judgement_criteria = idea_categories[category]
            break;
    if judgement_criteria is None:
        return {"error": "Could not fetch the judgement criteria for category "+ idea_category}
    
    # 5. adjust the scores are per the judgement criteria
    criteria_based_adjusted_scores = adjust_scores(transformed_scores_to_int, judgement_criteria)
    print ("criteria_based_adjusted_scores = ", criteria_based_adjusted_scores)

    #6. capture adjusted scores   

    judgement_tracker_collection = getjudgementtracker.get_judgment_tracker()
    print("judgement_tracker_collection = ", judgement_tracker_collection['judgement_tracker'])
    #print("jsonObj = ", request)
    idea_ids_in_judgement_tracker =  judgement_tracker_collection.keys()
    if(idea_id not in idea_ids_in_judgement_tracker):
        pass
    else:
        pass
        
    return {"status": "OK"}


def adjust_scores(assinged_scores:dict, judgement_criteria:dict) -> dict:
    percent_evalution_of_scores = {}
    percent_evalution_of_scores['idea_pitch'] = (judgement_criteria['idea_pitch']/100)*assinged_scores['idea_pitch']  
    
    if('efficiency_value' in assinged_scores.keys()):
        percent_evalution_of_scores['efficiency_value'] = (judgement_criteria['efficiency_value']/100)*assinged_scores['efficiency_value']  
    elif('feature_value' in assinged_scores.keys()):
        percent_evalution_of_scores['feature_value'] = (judgement_criteria['feature_value']/100)*assinged_scores['feature_value']
    elif('business_value' in assinged_scores.keys()):
        percent_evalution_of_scores['business_value'] = (judgement_criteria['business_value']/100)*assinged_scores['business_value']
        
    percent_evalution_of_scores['working_model'] = (judgement_criteria['working_model']/100)*assinged_scores['working_model']
    
    percent_evalution_of_scores['future_scope'] = (judgement_criteria['future_scope']/100)*assinged_scores['future_scope']
    
    percent_evalution_of_scores['presentation'] = (judgement_criteria['presentation']/100)*assinged_scores['presentation']
    
    return percent_evalution_of_scores