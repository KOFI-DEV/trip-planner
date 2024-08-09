from crewai import Task
from textwrap import dedent
from datetime import date


# key steps for task creation:
# 1. identify the desired outcome: define what success looks like for your project
# 2. taks breakdown: divide goal into smaller, managable tasks that agents can execute
# 3. assign tasks to agents: match agents with tasks based on their roles and experience

# task description template:
"""
def [task_name] (self, agent, [parameters]):
    return Task(description=dedent(f'''
    **Task** [a concise name or summary of the task]
    ))

"""


class TripTasks():

  def find_flights(self, agent, number_of_destinations, range):
    return Task(description=dedent(f"""
        Find cheapest flight tickets based on specific criterias. 
        Analyze and list together with total cost for one person {number_of_destinations} cheapest flights from Warsaw Chopin Airport and {number_of_destinations} cheapest flights from Warsaw Modlin Airport to european destinations.
        Travel range should be not more than {range} months from today. Departure should be either Thursday or Friday and return flight on Sunday or Monday.
        For each flight from the list specify airport, destination, departure and return dates, total cost and airline. Take into account only direct flights.
        
        {self.__tip_section()}
    """),
                agent=agent)

  def plan_city_tour(self, agent, destination, dates):
    return Task(description=dedent(f"""
        As a local expert on {destination} you must compile an 
        in-depth guide for someone traveling there and wanting 
        to have THE BEST trip ever!
        Gather information about  key attractions, local customs,
        special events, and daily activity recommendations.
        Find the best spots to go to, the kind of place only a
        local would know.
        This guide should provide a thorough overview of what 
        the city has to offer, including hidden gems, cultural
        hotspots, must-visit landmarks, weather forecasts, and
        high level costs.
        Make a list of bike rentals with google maps links. Recommended bicycle tracks and places worth to go by bicycle. 
        
        The final answer must be a comprehensive city guide, 
        rich in cultural insights and practical tips, 
        tailored to enhance the travel experience.
        {self.__tip_section()}

        Trip Date: {dates}
      """),
                agent=agent)

  def create_recomentation(self, agent, destination, dates):
    return Task(description=dedent(f"""
        Expand this guide into a a full travel 
        itinerary with detailed per-day plans, including 
        weather forecasts, places to eat, packing suggestions, 
        and a budget breakdown.
        
        You MUST suggest actual places to visit, actual bicycle tracks 
        to go and actual restaurants to go to.
        
        This itinerary should cover all aspects of the trip, 
        from arrival to departure, integrating the city guide
        information with practical travel logistics.
        
        Your final answer MUST be a complete expanded travel plan,
        formatted as markdown, encompassing a daily schedule,
        anticipated weather conditions, recommended bicycle rentals, and a detailed budget, ensuring THE BEST
        TRIP EVER, Be specific and give it a reason why you picked
        up each place, what make them special!
        {self.__tip_section()}

        Trip Date: {dates}
        Destination: {destination}
      """),
                agent=agent)

  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $1000!"