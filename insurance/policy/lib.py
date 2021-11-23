import pandas as pd
from insurance.settings import BASE_DIR

def get_policy_details(id):
    dataset = pd.read_csv(str(BASE_DIR) + '\policy\client_dataset.csv')
    dataset['Customer_id'] = dataset['Customer_id'].astype(str)
    dataset['Policy_id'] = dataset['Policy_id'].astype(str)
    dataset['Customer_Marital_status'] = dataset['Customer_Marital_status'].astype(str)
    dataset['Premium'] = dataset['Premium'].astype(str)
    dataset['bodily injury liability'] = dataset['bodily injury liability'].astype(str)
    dataset['personal injury protection'] = dataset['personal injury protection'].astype(str)
    dataset['property damage liability'] = dataset['property damage liability'].astype(str)
    dataset['collision'] = dataset['collision'].astype(str)
    dataset['comprehensive'] = dataset['comprehensive'].astype(str)

    # filter on the basis of customer id or policy id
    print(dataset['Policy_id'].dtype)
    policy = dataset[(dataset['Policy_id'] == id) | (dataset['Customer_id'] == id)]
    return policy
