from flask import Flask, jsonify, send_from_directory, request
import pandas as pd
from flask_cors import CORS
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
CORS(app, resources={r"/plot": {"origins": "http://localhost:3000"}})

# Load the data from a relative path
data_file = os.path.join(os.path.dirname(__file__), 'df_clean.csv')
df = pd.read_csv(data_file)

# Data preprocessing and analysis (your code here)
df_clean = pd.DataFrame(df)

# Serve the cleaned data as JSON
@app.route('/data')
def get_clean_data():
    return jsonify(df_clean.to_dict(orient='records'))

# Generate and serve the plot
# plot
@app.route('/plot')  # Corrected route definition
def generate_plot():
    try:
        plt.figure(figsize=(6, 6))
        plt.title("Value Counts of The Type Variable")
        sns.set(style="darkgrid")
        ax = sns.countplot(x="type", data=df, palette="Pastel2")
        ax.bar_label(ax.containers[0])      

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot.png')

    except Exception as e:
        return jsonify({'error': str(e)})
    
# 1
@app.route('/plot1')  # Corrected route definition
def generate_plot1():
    try:
        plt.figure(figsize=(30,6))
        plt.title("Value Counts of The Ratings Variable")
        sns.set(style="darkgrid")
        ax = sns.countplot(x="rating", data=df, palette="Pastel2")
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot1.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot1.png')

    except Exception as e:
        return jsonify({'error': str(e)})

# 2
# 2
@app.route('/plot2')  # Corrected route definition
def generate_plot2():
    try:
        plt.figure(figsize=(12, 3))
        plt.title("Value Counts of The Categories Variable")
        sns.set(style="darkgrid")
        ax = sns.countplot(x='categories', data=df, palette="Pastel2", order=df['categories'].value_counts().iloc[:5].index)
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot2.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot2.png')

    except Exception as e:
        return jsonify({'error': str(e)})

    
# 3
@app.route('/plot3')  # Corrected route definition
def generate_plot3():
    try:
        plt.figure(figsize=(12,2))
        plt.title("Value Counts of The Country Variable")
        sns.set(style="darkgrid")
        ax = sns.countplot(x="country", data=df, palette="Pastel2", order=df.country.value_counts().iloc[:4].index)
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot3.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot3.png')

    except Exception as e:
        return jsonify({'error': str(e)})
    
# 4
@app.route('/plot4')  # Corrected route definition
def generate_plot4():
    try:
        plt.figure(figsize=(12,3))
        plt.title("Value Counts of The Director Variable")
        sns.set(style="darkgrid")
        ax = sns.countplot(x="director", data=df, palette="Pastel2", order=df.director.value_counts().iloc[:6].index)
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot4.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot4.png')

    except Exception as e:
        return jsonify({'error': str(e)})   


    
# 5
@app.route('/plot5')  # Corrected route definition
def generate_plot5():
    try:
        plt.figure(figsize=(12, 3))
        plt.title("Count of Shows Added by Date")
        sns.set(style='darkgrid')
        ax = sns.countplot(data=df, x="date_added", palette="Pastel2")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot5.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot5.png')

    except Exception as e:
        return jsonify({'error': str(e)})

    

# 6
@app.route('/plot6')  # Corrected route definition
def generate_plot6():
    try:
        plt.figure(figsize=(12, 3))
        plt.title("Value Counts of The Release Year Variable")
        sns.set(style='darkgrid')
        ax = sns.countplot(data=df, x="release_year", palette="Pastel2", order=df['release_year'].value_counts().iloc[:6].index)
        ax.bar_label(ax.containers[0])

        # Save the plot as an image
        image_path = os.path.join(os.path.dirname(__file__), 'plot6.png')
        plt.savefig(image_path, format='png')
        plt.close()

        # Serve the saved image
        return send_from_directory(os.path.dirname(__file__), 'plot6.png')

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)










































'''
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# from flask import Flask, jsonify, send_from_directory
# import io


# app = Flask(__name__)   

# # Input
# df=pd.read_csv('amazon_prime_titles.csv')
# df
# df.rename(columns={'listed_in':'categories'},inplace=True)
# df


# # Drop the columns that we wont't to involved in analysis
# df.drop(['show_id'], axis=1, inplace= True)
# df.drop(['description'],axis=1 , inplace=True)
# df


# # Sneak peek data
# df.shape
# df.info()
# df.describe(include = object)


# # Handling Duplicate Values 
# df.duplicated().sum()
# df.isnull().sum()

# df['director'].fillna('Unavailable',inplace=True)
# df['cast'].fillna('Unavailable',inplace=True)
# df['country'].fillna('Unavailable',inplace=True)
# df['rating']=df['rating'].fillna(df['rating'].mode()[0])
# df['date_added']=df['date_added'].ffill()
# df

# df['date_added']=pd.to_datetime(df['date_added'], format='%B %d, %Y')
# df     

                         
# df.isnull().sum()


                                
# # Save Clean data in csv format
# df_clean=pd.DataFrame(df)
# df_clean.to_csv("df_clean.csv")
# df_clean



# # Exploratory Data Analysis
# df.type.value_counts()
# df.type.value_counts(normalize=True)

# #Number of show type vriable
# @app.route('/plot')
# def plot():

#     plt.figure(figsize=(6,6))
#     plt.title("Value Counts of The Type Variable")
#     sns.set(style="darkgrid")
#     ax = sns.countplot(x="type", data=df, palette="Pastel2")
#     ax.bar_label(ax.containers[0])

#     # Specify the file path where you want to save the plot
#     image_path = 'C:\\self made\\python_analysis\\backend\\plot.png'

#     # Save the plot as an image
#     plt.savefig(image_path, format='png')


#     # Serve the saved image
#     return send_from_directory('.', 'plot.png')



# # DataVisualization=ax.to_html()
# # @app.route('/api/DataVisualization')
# # def det_DataVisualization():
# #     return DataVisualization

# # #Number of Ratings Variable
# # plt.figure(figsize=(30,6))
# # plt.title("Value Counts of The Ratings Variable")
# # sns.set(style="darkgrid")
# # ax = sns.countplot(x="rating", data=df, palette="Pastel2")
# # ax.bar_label(ax.containers[0])


#3 # #Categories
# plt.figure(figsize=(12,3))
# plt.title("Value Counts of The Categories Variable")
# sns.set(style="darkgrid")
# ax = sns.countplot(x='categories', data=df, palette="Pastel2", order=df.categories.value_counts().iloc[:5].index)
# ax.bar_label(ax.containers[0])


#4 # #Number of Show by Country
# plt.figure(figsize=(12,2))
# plt.title("Value Counts of The Country Variable")
# sns.set(style="darkgrid")
# ax = sns.countplot(x="country", data=df, palette="Pastel2", order=df.country.value_counts().iloc[:4].index)
# ax.bar_label(ax.containers[0])


# 6 # # Date Added by Show
# sns.set(style='darkgrid')
# sns.displot(data = df ,x="date_added")
# plt.xticks(rotation = 45, ha = 'right')


#7 # # Number of Show Year by Year
# sns.set(style='darkgrid')
# ax = sns.displot(data = df ,x="release_year", height=4,aspect=2)
   

# if __name__ == '__main__':
#     app.run(debug=True)'''