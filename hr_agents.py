{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7c9b5448-1d95-41bc-94a0-9dc09d3d263a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All required packages installed successfully!\n"
     ]
    }
   ],
   "source": [
    "!pip install langgraph langchain-openai fastapi uvicorn python-dotenv aiosqlite sqlalchemy pydantic streamlit --quiet\n",
    "\n",
    "print(\"All required packages installed successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "19c7948f-2f48-4a60-8475-c2cfac9a455c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: langgraph in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (1.1.8)\n",
      "Requirement already satisfied: pandas in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: langchain-core<2,>=1.3.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (1.3.0)\n",
      "Requirement already satisfied: langgraph-checkpoint<5.0.0,>=2.1.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (4.0.2)\n",
      "Requirement already satisfied: langgraph-prebuilt<1.1.0,>=1.0.9 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (1.0.10)\n",
      "Requirement already satisfied: langgraph-sdk<0.4.0,>=0.3.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (0.3.13)\n",
      "Requirement already satisfied: pydantic>=2.7.4 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (2.10.3)\n",
      "Requirement already satisfied: xxhash>=3.5.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph) (3.6.0)\n",
      "Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (1.33)\n",
      "Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (0.7.32)\n",
      "Requirement already satisfied: packaging>=23.2.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (24.2)\n",
      "Requirement already satisfied: pyyaml<7.0.0,>=5.3.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (6.0.2)\n",
      "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (9.0.0)\n",
      "Requirement already satisfied: typing-extensions<5.0.0,>=4.7.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (4.15.0)\n",
      "Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langchain-core<2,>=1.3.0->langgraph) (0.14.1)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core<2,>=1.3.0->langgraph) (2.1)\n",
      "Requirement already satisfied: ormsgpack>=1.12.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph-checkpoint<5.0.0,>=2.1.0->langgraph) (1.12.2)\n",
      "Requirement already satisfied: httpx>=0.25.2 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph) (0.28.1)\n",
      "Requirement already satisfied: orjson>=3.11.5 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph) (3.11.8)\n",
      "Requirement already satisfied: requests-toolbelt>=1.0.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2,>=1.3.0->langgraph) (1.0.0)\n",
      "Requirement already satisfied: requests>=2.0.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2,>=1.3.0->langgraph) (2.32.3)\n",
      "Requirement already satisfied: zstandard>=0.23.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core<2,>=1.3.0->langgraph) (0.23.0)\n",
      "Requirement already satisfied: anyio in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (4.7.0)\n",
      "Requirement already satisfied: certifi in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (2025.4.26)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (1.0.9)\n",
      "Requirement already satisfied: idna in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (3.7)\n",
      "Requirement already satisfied: h11>=0.16 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from httpcore==1.*->httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (0.16.0)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pydantic>=2.7.4->langgraph) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.27.1 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pydantic>=2.7.4->langgraph) (2.27.1)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pandas) (2.1.3)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2,>=1.3.0->langgraph) (3.3.2)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2,>=1.3.0->langgraph) (2.3.0)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (from anyio->httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (1.3.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install langgraph pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1d6d3771-1610-4e41-a7c4-fac7987fe5a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nest_asyncio in c:\\users\\rajoo\\anaconda3\\lib\\site-packages (1.6.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install nest_asyncio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c103905f-331d-4c3d-a444-27069602fa64",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langgraph.graph import StateGraph, END\n",
    "from typing import TypedDict, List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1c56472c-da63-40d1-8fdf-b65f5ad79ddb",
   "metadata": {},
   "outputs": [],
   "source": [
    "class AgentState(TypedDict):\n",
    "    resume_text: str\n",
    "    ats_score: int\n",
    "    stage: str\n",
    "    interview_qa: List[dict]\n",
    "    screening: dict\n",
    "    meeting_link: str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7a0ec867-61df-4964-816f-4e9fbc9ef9ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ats_agent(state):\n",
    "    resume = state[\"resume_text\"]\n",
    "    \n",
    "    score = 0\n",
    "    if \"Python\" in resume:\n",
    "        score += 40\n",
    "    if \"FastAPI\" in resume:\n",
    "        score += 40\n",
    "    if \"SQL\" in resume:\n",
    "        score += 20\n",
    "    \n",
    "    state[\"ats_score\"] = score\n",
    "    state[\"stage\"] = \"interview\" if score >= 80 else \"rejected\"\n",
    "    \n",
    "    return state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "579b056f-0179-45bf-a799-c5e636722346",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interview_agent(state):\n",
    "    questions = [\n",
    "        \"What is Python?\",\n",
    "        \"Explain FastAPI\",\n",
    "        \"What is API?\"\n",
    "    ]\n",
    "    \n",
    "    qa = []\n",
    "    \n",
    "    for q in questions:\n",
    "        answer = \"demo answer\"\n",
    "        score = 8\n",
    "        \n",
    "        qa.append({\n",
    "            \"question\": q,\n",
    "            \"answer\": answer,\n",
    "            \"score\": score\n",
    "        })\n",
    "    \n",
    "    state[\"interview_qa\"] = qa\n",
    "    state[\"stage\"] = \"screening\"\n",
    "    \n",
    "    return state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b5bd3c60-9e01-41a5-8e66-06c6334b0bd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def screening_agent(state):\n",
    "    state[\"screening\"] = {\n",
    "        \"notice_period\": \"30 days\",\n",
    "        \"joining\": \"Immediate\"\n",
    "    }\n",
    "    \n",
    "    state[\"stage\"] = \"scheduled\"\n",
    "    \n",
    "    return state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a083c0eb-90c1-4142-a935-1a9ad8f46cfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scheduling_agent(state):\n",
    "    state[\"meeting_link\"] = \"https://meet.google.com/demo\"\n",
    "    return state"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9fe19680-99c1-4e37-9587-30108b6c4fef",
   "metadata": {},
   "outputs": [],
   "source": [
    "graph = StateGraph(AgentState)\n",
    "\n",
    "graph.add_node(\"ats\", ats_agent)\n",
    "graph.add_node(\"interview\", interview_agent)\n",
    "graph.add_node(\"screening\", screening_agent)\n",
    "graph.add_node(\"schedule\", scheduling_agent)\n",
    "\n",
    "graph.set_entry_point(\"ats\")\n",
    "\n",
    "graph.add_edge(\"ats\", \"interview\")\n",
    "graph.add_edge(\"interview\", \"screening\")\n",
    "graph.add_edge(\"screening\", \"schedule\")\n",
    "graph.add_edge(\"schedule\", END)\n",
    "\n",
    "recruitment_graph = graph.compile()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a44aa18c-d9ad-44f9-9861-573635d2cf37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'resume_text': 'I know Python FastAPI SQL', 'ats_score': 100, 'stage': 'scheduled', 'interview_qa': [{'question': 'What is Python?', 'answer': 'demo answer', 'score': 8}, {'question': 'Explain FastAPI', 'answer': 'demo answer', 'score': 8}, {'question': 'What is API?', 'answer': 'demo answer', 'score': 8}], 'screening': {'notice_period': '30 days', 'joining': 'Immediate'}, 'meeting_link': 'https://meet.google.com/demo'}\n"
     ]
    }
   ],
   "source": [
    "result = recruitment_graph.invoke({\n",
    "    \"resume_text\": \"I know Python FastAPI SQL\"\n",
    "})\n",
    "\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60a03e7b-d20e-4895-ad09-4d1edc051242",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65b1a605-e709-4340-bf4c-522b47952574",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ceae8bb7-1ead-4039-b6f3-9bf88b4250ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "db = pd.DataFrame(columns=[\n",
    "    \"resume\", \"ats_score\", \"stage\"\n",
    "])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7a8944ab-d908-4eca-8734-adc4d2afa601",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>resume</th>\n",
       "      <th>ats_score</th>\n",
       "      <th>stage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      resume  ats_score      stage\n",
       "0  I know Python FastAPI SQL        100  scheduled"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db.loc[len(db)] = [\n",
    "    result[\"resume_text\"],\n",
    "    result[\"ats_score\"],\n",
    "    result[\"stage\"]\n",
    "]\n",
    "\n",
    "db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "aea5f1fe-1cd9-4ecc-bd87-7d16f2421235",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HR DASHBOARD\n",
      "                      resume  ats_score      stage\n",
      "0  I know Python FastAPI SQL        100  scheduled\n"
     ]
    }
   ],
   "source": [
    "print(\"HR DASHBOARD\")\n",
    "print(db)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "38bc7f23-5877-4ffa-b390-12eb9c88b125",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>resume</th>\n",
       "      <th>ats_score</th>\n",
       "      <th>stage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      resume  ats_score      stage\n",
       "0  I know Python FastAPI SQL        100  scheduled"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Filter shortlisted\n",
    "db[db[\"stage\"] == \"scheduled\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4a0cfc4d-67be-43ea-8f0a-ee5931c12e03",
   "metadata": {},
   "outputs": [],
   "source": [
    "def hr_chatbot(query):\n",
    "    \n",
    "    if \"all candidates\" in query:\n",
    "        return db\n",
    "    \n",
    "    if \"selected\" in query:\n",
    "        return db[db[\"stage\"] == \"scheduled\"]\n",
    "    \n",
    "    if \"rejected\" in query:\n",
    "        return db[db[\"stage\"] == \"rejected\"]\n",
    "    \n",
    "    return \"No data found\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "4b25d240-4537-4987-bcd6-7c305b271a8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>resume</th>\n",
       "      <th>ats_score</th>\n",
       "      <th>stage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      resume  ats_score      stage\n",
       "0  I know Python FastAPI SQL        100  scheduled"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr_chatbot(\"show all candidates\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "12214147-755c-44eb-8e49-0b06f23292ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'total_candidates': 1, 'selected': 1, 'rejected': 0}"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def role_summary():\n",
    "    return {\n",
    "        \"total_candidates\": len(db),\n",
    "        \"selected\": len(db[db[\"stage\"] == \"scheduled\"]),\n",
    "        \"rejected\": len(db[db[\"stage\"] == \"rejected\"])\n",
    "    }\n",
    "\n",
    "role_summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8aefcde2-5abd-4397-bb61-dfb17f80b872",
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_demo():\n",
    "    resume = \"I know Python FastAPI SQL\"\n",
    "    \n",
    "    result = recruitment_graph.invoke({\n",
    "        \"resume_text\": resume\n",
    "    })\n",
    "    \n",
    "    print(\"Pipeline Output:\", result)\n",
    "    \n",
    "    # Save\n",
    "    db.loc[len(db)] = [\n",
    "        result[\"resume_text\"],\n",
    "        result[\"ats_score\"],\n",
    "        result[\"stage\"]\n",
    "    ]\n",
    "    \n",
    "    print(\"\\nDashboard:\")\n",
    "    print(db)\n",
    "    \n",
    "    print(\"\\nChatbot Query:\")\n",
    "    print(hr_chatbot(\"show all candidates\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5e719c32-bd15-47dd-9fd4-737d1ff55ba5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pipeline Output: {'resume_text': 'I know Python FastAPI SQL', 'ats_score': 100, 'stage': 'scheduled', 'interview_qa': [{'question': 'What is Python?', 'answer': 'demo answer', 'score': 8}, {'question': 'Explain FastAPI', 'answer': 'demo answer', 'score': 8}, {'question': 'What is API?', 'answer': 'demo answer', 'score': 8}], 'screening': {'notice_period': '30 days', 'joining': 'Immediate'}, 'meeting_link': 'https://meet.google.com/demo'}\n",
      "\n",
      "Dashboard:\n",
      "                      resume  ats_score      stage\n",
      "0  I know Python FastAPI SQL        100  scheduled\n",
      "1  I know Python FastAPI SQL        100  scheduled\n",
      "\n",
      "Chatbot Query:\n",
      "                      resume  ats_score      stage\n",
      "0  I know Python FastAPI SQL        100  scheduled\n",
      "1  I know Python FastAPI SQL        100  scheduled\n"
     ]
    }
   ],
   "source": [
    "full_demo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "bdc10908-5598-49f9-a769-fe91e687e115",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>resume</th>\n",
       "      <th>ats_score</th>\n",
       "      <th>stage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      resume  ats_score      stage\n",
       "0  I know Python FastAPI SQL        100  scheduled\n",
       "1  I know Python FastAPI SQL        100  scheduled"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "148da117-2b6f-4006-97cd-dfe6e5c203ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>resume</th>\n",
       "      <th>ats_score</th>\n",
       "      <th>stage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>I know Python FastAPI SQL</td>\n",
       "      <td>100</td>\n",
       "      <td>scheduled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      resume  ats_score      stage\n",
       "0  I know Python FastAPI SQL        100  scheduled\n",
       "1  I know Python FastAPI SQL        100  scheduled"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hr_chatbot(\"show all candidates\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12e1b5fc-0a8a-49fd-8eff-e625090e84ad",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
