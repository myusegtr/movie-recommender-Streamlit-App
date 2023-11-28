#Imports
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

#1. Title and Subheader
st.title("Data Analysis movie recommender system")
st.subheader("Data Analysis Using Python & Streamlit")


#2. Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data=pd.read_csv(upload)


#3. Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        
        
#4. Check DataType of Each Column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

# Finding unique labels in tagline column
if upload is not None:
    if st.checkbox("Find unique labels in tagline column"):
        st.text("List of unique labels")
        st.write(data['tagline'].nunique())
        st.write(data['tagline'].unique())

#Extracting country from the release date
# if upload is not None:
#     if st.checkbox("length of first row"):
        
#         st.write(len(str(data['release_date'].head(2))))


if upload is not None:
    if st.checkbox("Create a separate country column"):
        st.text("Country")
        if str(data['release_date']).find("India")==True:
            data['country']=data['release_date'].str[-6:-1]
        else:
            data['country']=data['release_date'].str[-4:-1]                    
        st.write(data['country'].head(4))
        st.write(sns.countplot(data['country']))

#5. Find Shape of Our Dataset (Number of Rows And Number of Columns)
if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?",('Rows',
                                                                'Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

#6. Finding the general info & statistical analysis of the dataset.

if upload is not None:
    if st.checkbox("General info of the dataset"):
        st.text("Info")
        st.write(data.info())
    if st.checkbox("Statistical summary of the dataset"):
        st.text("Description")
        st.write(data.describe())    


#7. Find Null Values in The Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            #sns.heatmap(data.isna().sum())
            #data.fillna(0) --To fill null values with zero
            st.pyplot()
    else:
        st.success("No Missing Values")
        

#8. Data cleaning part
if upload is not None:
    if st.checkbox("Find & remove duplicate rows"):
        st.text("Find Duplicates")
        st.write(sum(data.duplicated()))
        st.text("Removing duplicates")
        data.drop_duplicates(inplace=True)
        st.text("Shape of dataset after removing duplicate rows")
        st.write(data.shape)

if upload is not None:
    if st.checkbox("Changing release date to date time format"):
        st.text("Datetype conversion")
        data[['release_date']]=pd.to_datetime(data['release_date'])
        st.text("New release date format")
        st.write(data['release_date'].head(5))

#Dropping unwanted columns
# if upload is not None:
#     if st.checkbox("Drop columns"):
#         st.text("Dropping some unwanted columns")
#         st.write(data.drop(['tagline','wins_nominations'],axis=1,inplace=True))
#         st.write(data.shape)
#         sns.heatmap(data.isnull())
#         st.pyplot()

if upload is not None:
    if st.checkbox("Drop columns"):
        st.text("Dropping some unwanted columns")
        st.write(data.drop(['title','is_adult'],axis=1,inplace=True))
        st.write(data.shape)
        sns.heatmap(data.isnull())
        st.pyplot()


# Dropping some unwanted rows
if upload is not None:
    if st.checkbox("Delete rows which has missing values"):
        st.text("Deleted")
        st.write(data.dropna(how='any',inplace=True))
        sns.heatmap(data.isnull())
        st.pyplot()        

# #Check for incorrect values in the rows
# #if upload is not None:
#     if st.checkbox("Row checking"):
#         st.text("Rows with incorrect values in the budget column")
#         st.write(data[(data['budget']==0)].shape[0])
#         st.text("Rows with incorrect values in the revenue column")
#         st.write(data[(data['revenue']==0)].shape[0])

# now extracting year & month from the release date.
if upload is not None:
    if st.checkbox("Year & month"):
        st.text("Getting year & month column ")
        #Convert release date to date time format
        data['release_date'] = pd.to_datetime(data['release_date'], format='%d %B %Y', errors='coerce')
        data['year'] = data['release_date'].dt.year
        data['month'] = data['release_date'].dt.month_name()
        st.write(data[['year','month']].head(5))
        st.write(data.columns)
# if upload is not None:
#     if st.checkbox("Year & month"):
#         st.text("Getting year & month column ")
#         # Convert release date to date time format
#         data['release_date'] = pd.to_datetime(data['release_date'], format='%d %B %Y', errors='coerce')

#         # Check for unconverted values
#         unconverted_rows = data[data['release_date'].isna()]
#         if not unconverted_rows.empty:
#             st.warning(f"Unable to convert the following rows to datetime:\n{unconverted_rows}")

#         # Extract year and month into separate columns
#         data['year'] = data['release_date'].dt.year
#         data['month'] = data['release_date'].dt.month_name()
        
#         st.write(data[['year', 'month']].head(5))
#         st.write(data.columns)


                







#7. Find Duplicate Values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    
#8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

##########################################################################################
#Now visualizing the data

# Split actors into individual names
import numpy as np

if upload is not None:
    if st.checkbox("Actors_list"):
       actor_lists = data['actors'].str.split('|')
       st.write(actor_lists)
       
       # Flatten the lists of actors
       all_actors = [actor for sublist in actor_lists for actor in sublist]
       
       # Create a DataFrame with actor counts
       actor_counts = pd.Series(all_actors).value_counts().reset_index()
       
       # Rename columns for clarity
       actor_counts.columns = ['Actor', 'MovieCount']
       
       # Display the top 20 actors
       top_20_actors = actor_counts.head(20)
       st.write(top_20_actors)
       
       # Create a bar chart for the top 20 actors
       st.bar_chart(top_20_actors.set_index('Actor'))

# Movie count year wise
if upload is not None:
    if st.checkbox("Movie count year wise"):
        st.text("year vs movie_count")
        movie_count_per_year=data['year_of_release'].value_counts().reset_index()
        movie_count_per_year.columns=['year_of_release', 'movie_count']
        st.write(movie_count_per_year)
        st.bar_chart(movie_count_per_year.set_index('year_of_release'))

# Movie count genre wise
if upload is not None:
    if st.checkbox("Movie count genre wise"):
        st.text("genre vs movie_count")
        movie_count_by_genre = data['genres'].value_counts().reset_index()
        movie_count_by_genre.columns=['genres', 'movie_count']
        st.text("finding popular genre by movie count")
        st.write(movie_count_by_genre)
        st.bar_chart(movie_count_by_genre.set_index('genres'))

#some data processing
if upload is not None:
    if st.checkbox("Max & Min movie runtime/length"):
        # max_runtime_index = data['runtime'].idxmax()
        # st.write(data.loc[max_runtime_index])
        # st.text("Record with min runtime")
        # min_runtime_index = data['runtime'].idxmin()
        # st.write(data.loc[min_runtime_index])
        default_value=90
        data['runtime'] = pd.to_numeric(data['runtime'], errors='coerce').fillna(default_value).astype(int)
        max=data['runtime'].astype(int).max()
        min=data['runtime'].astype(int).min()
        st.text("Record with max runtime")
        st.write(data[data['runtime']==max])
        st.text("Record with min runtime")
        st.write(data[data['runtime']==min])

     
# Line chart for finding relation between rating & imdb votes
if upload is not None:
    if st.checkbox("Finding some relation between movie rating & Imdb votes"):
       st.text("rating vs votes")
       st.line_chart(data[['imdb_rating','imdb_votes']])
     

if upload is not None:
    if st.checkbox("dropping rows with null values"):
       st.text("Shape of dataset before dropping rows") 
       st.write(data.shape)
       st.text("shape of dataset after dropping certain rows")    
       data.dropna(inplace=True)
       st.write(data.shape)


#########################################################################################################


#9. About Section

if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")


#10. By
if st.checkbox("By"):
    st.success("Aaradhya kumar")


#download updated file

if st.button('Save DataFrame'):
    open('data_streamlit.csv','w').write(data.to_csv())
    st.text("Saved To local Drive")