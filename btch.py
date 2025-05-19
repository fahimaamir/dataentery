import pandas as pd
import streamlit as st

    #if st.session_state.newrecord==0 :
df = pd.DataFrame(    {        "sno": [       None  ],        "sname": [     None    ],        " sfee": [     0   ]   })
newrecord1 = st.data_editor(df,num_rows="dynamic",key="demo_df")


if st.button("New Record"):
    ttt2 = pd.DataFrame(newrecord1) 
    #xtrain = df.loc[df['sno'].notnull(),['sname','sfee' ]]
    #my_df2= ttt2[(ttt2['sno'] != isnull())]
    df_no_null = ttt2[ttt2['sno'].notna()]
    #df_no_null1 = (df_no_null[len(df_no_null['sno'])])
    #df_no_null1 = df_no_null['sno'].astype(str).map(len)
    rslt_df = df_no_null.loc[df_no_null['sno'].astype(str).map(len) >0]
    st.write(rslt_df)
  #         df['ZipLen'] = df['ZipCode'].astype(str).map(len)
#df['ZipLen'] = np.floor(np.log10(df['ZipCode'].values)).astype(int) + 1
#df['EventCount'] = df['Event'].str.split("/").str.len()
    #filter1 = ttt2[ttt2['sno'] != isnull())]
    #xtrain = df[df['Survive'].notnull(), ['Age','Fare', 'Group_Size','deck', 'Pclass', 'Title' ]]
    #new_df = ttt2.loc[df['sno'].notna()]
#    new_df = ttt2.loc[df['sno']]
    #st.write(df_no_null)    
    
    st.write("save")    
    
        
    