import pandas as pd
import os
import re
import sys






def generate_md(full_name):
    '''
    input(s): full_name (str)
    output(s): -
    description: generates an md file for a contributor based on their full name in the google form response.
    '''
    df = pd.read_csv('./data/google-form-responses.csv') # access google form responses using google sheets API or URL - still figuring out
    
    if not (full_name in df['Full name for website'].tolist()):
        raise ValueError('Not a contributor')
        
    if os.path.exists(f'{full_name}.md'):
        raise Exception('This contributor already has a published page. You do not have permission to update their information.')
        
        
    contributor_response = df[df['Full name for website'] == full_name]
        
    title = contributor_response['What is the title of your submission?'].iloc[0]
    date = contributor_response['Timestamp'].iloc[0]
    categories = contributor_response['What is the primary topic (e.g., data visualization, ethics, machine learning)'].iloc[0]
    tags = contributor_response['List any other key words or tags that you think are emphasized in your submission (e.g., Python, R, ggplot, diversity, regression, MatPlotLib, tree models, etc).'].iloc[0]
    
        
    with open(f'./_posts/{full_name}.md', 'w') as my_file: # name of the file needs to be in a certain format with the date first - fix
        my_file.write('---\n')
        my_file.write(f'title: {title}\n')
        my_file.write(f'date: {date}\n')
        my_file.write(f'categories: [{categories}]\n') # should be a list
        my_file.write(f'tags: [{tags}]\n') # should be a list and all lowercase
        my_file.write('---\n')
        
        my_file.write('\n')
        
        my_file.write('### Description\n')
        description = contributor_response['Please provide a one-paragraph summary of your contribution.'].iloc[0]
        my_file.write(description)
        
        # not yet finished but the page layout should follow the above structure
        
    print(f'Created a page for {full_name}')



if __name__ == "__main__":
    name = input('Enter the name of a contributor: ')
    generate_md(name)