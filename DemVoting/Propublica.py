import json
import requests

api_token = 'xyCBpSekq2h43E0G1U4moLQVQMXCL9PZrF8cT2wA'
api_url_base = 'https://api.propublica.org/congress/v1/'

headers = {'Content-Type': 'application/json',
           'X-API-Key': api_token}




def get_members(congress = 116, chamber = 'senate'):

	api_url = api_url_base + f"{congress}/{chamber}/members.json"

	response = requests.get(api_url, headers=headers)


	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None


def compare_members(member1_id, member2_id, congress = 116, chamber = 'senate'):

	api_url = api_url_base + f'members/{member1_id}/votes/{member2_id}/{congress}/{chamber}.json'

	response = requests.get(api_url, headers=headers)

	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None


def compare_cosponsorship(member1_id, member2_id, congress = 116, chamber = 'senate'):

	api_url = api_url_base + f'members/{member1_id}/bills/{member2_id}/{congress}/{chamber}.json'

	response = requests.get(api_url, headers=headers)

	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None



jsonMembers = get_members()

members = jsonMembers.get("results")[0].get('members')

candidates = ["Booker", "Gillibrand", "Harris", "Klobuchar", "Sanders", "Warren"]

candidate_ids = [x.get("id") for x in members if x.get('last_name') in candidates]


#vote_comparison_table = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

#for i in range(0,6):
#	for j in range(0,6):
#		vote_comparison_table[i][j] = compare_members(candidate_ids[i], candidate_ids[j]).get('results')[0].get('agree_percent')

#print(vote_comparison_table)

cosponsor_comparison_table = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

for i in range(0,6):
	for j in range(0,6):
		cosponsor_comparison_table[i][j] = len(compare_cosponsorship(candidate_ids[i], candidate_ids[j]).get('results')[0].get('bills'))




print(cosponsor_comparison_table)




