crew_details={
    'pilot':'varma',
    'co-pilot':'punith',
    'stewardes':'reeta'
    }
print('before update')
print('co-pilot:',crew_details['co-pilot'])

crew_details.update({'flight attendant':'veeresh','co-pilot':'prashanth'})

print('after update')
print('co-pilot:',crew_details['co-pilot'])
print(list(crew_details))   

   
    
