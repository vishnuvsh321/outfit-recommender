import pandas as pd
from recommender.model import recommmend_outfit

def test_recommend_outfit():
    df=pd.DataFrame({'Occasion':['Work','Party','Sport','Casual','Formal',],'Outfit':['Jacket','Jeans','Shirt','Shorts','Sweater']})
    assert recommmend_outfit({'Ocassion':'Work'},df) == 'Jacket'