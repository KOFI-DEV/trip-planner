# Date: 07-Aug-2024
# definition of agents 
# ----------------------------------------

from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

# Expert Travel Agent
# Flight Researcher
# City guide


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

class TripPlannerAgents():

    def flight_selection_expert(self):
        return Agent(
            role="Flight Selection Expert ",
            backstory=dedent(f"""An expert in researching and selecting best flight deals available."""),
            goal=dedent(f"""
                        Find and list together with total cost for one person 5 cheapest flights from Warsaw Chopin Airport and 5 cheapest flights from Warsaw Modlin Airport to european destinations. Travel range should be not more than three months from today. Departure should be either Thursday or Friday and return flight on Sunday or Monday. For each flight from the list specify airport, destination, departure and return dates, total cost and airline. Take into account only direct flights. """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_guide(self):
        return Agent(
            role="Local Expert at this city.",
            backstory=dedent(f"""
                             Local resident and expert City Guide which loves exploring city on a bicyckle.
                             """),
            goal=dedent(f"""Provide the BEST insights about the selected city. Include events happening during provided range of dates. Please make a list of bike rentals and recommended bicycle tracks near by."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. I have decades of experience making travel inteneries."""),
            goal=dedent(f"""
                        Create a 3 to 4-day travel itinarary that will contain direct flight details and comprehensive plan for each day, include budget, suggest bike rentals in the area and highlight events that will take place during this period of time
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

   