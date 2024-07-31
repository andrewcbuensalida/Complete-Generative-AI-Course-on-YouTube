[
    HumanMessage(
        content="what is the weather in sf", id="ad1ffe65-14f3-49c7-aea3-36fa22e2f75b"
    ),
    AIMessage(
        content="",
        additional_kwargs={
            "tool_calls": [
                {
                    "id": "call_2GRyJg2xZf1nZYgQ2FM5YQta",
                    "function": {
                        "arguments": '{"query":"weather in San Francisco"}',
                        "name": "search",
                    },
                    "type": "function",
                }
            ]
        },
        response_metadata={
            "token_usage": {
                "completion_tokens": 16,
                "prompt_tokens": 49,
                "total_tokens": 65,
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": None,
            "finish_reason": "tool_calls",
            "logprobs": None,
        },
        id="run-9573e4ed-58ed-412d-bf4f-6d28eb9a32a1-0",
        tool_calls=[
            {
                "name": "search",
                "args": {"query": "weather in San Francisco"},
                "id": "call_2GRyJg2xZf1nZYgQ2FM5YQta",
                "type": "tool_call",
            }
        ],
        usage_metadata={"input_tokens": 49, "output_tokens": 16, "total_tokens": 65},
    ),
    ToolMessage(
        content='["It\'s 60 degrees and foggy."]',
        name="search",
        id="4b5114c5-c7a6-4394-b4b6-da0cd997411d",
        tool_call_id="call_2GRyJg2xZf1nZYgQ2FM5YQta",
    ),
    AIMessage(
        content="The weather in San Francisco is currently 60 degrees and foggy.",
        response_metadata={
            "token_usage": {
                "completion_tokens": 15,
                "prompt_tokens": 82,
                "total_tokens": 97,
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": None,
            "finish_reason": "stop",
            "logprobs": None,
        },
        id="run-b92b95af-3493-49fa-aec9-85d98c42ddb8-0",
        usage_metadata={"input_tokens": 82, "output_tokens": 15, "total_tokens": 97},
    ),
    HumanMessage(
        content="what is the weather in sf", id="19d36641-45a4-40b3-bd3a-8603cc695f0a"
    ),
    AIMessage(
        content="",
        additional_kwargs={
            "tool_calls": [
                {
                    "id": "call_IO05ClWhWGAlg7nLExQiMrcY",
                    "function": {
                        "arguments": '{"query":"weather in San Francisco"}',
                        "name": "search",
                    },
                    "type": "function",
                }
            ]
        },
        response_metadata={
            "token_usage": {
                "completion_tokens": 16,
                "prompt_tokens": 110,
                "total_tokens": 126,
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": None,
            "finish_reason": "tool_calls",
            "logprobs": None,
        },
        id="run-f12f73f2-dc93-4476-a4fa-4679139a72eb-0",
        tool_calls=[
            {
                "name": "search",
                "args": {"query": "weather in San Francisco"},
                "id": "call_IO05ClWhWGAlg7nLExQiMrcY",
                "type": "tool_call",
            }
        ],
        usage_metadata={"input_tokens": 110, "output_tokens": 16, "total_tokens": 126},
    ),
    ToolMessage(
        content='["It\'s 60 degrees and foggy."]',
        name="search",
        id="029c4839-2267-451e-b8b9-42b77077ba2b",
        tool_call_id="call_IO05ClWhWGAlg7nLExQiMrcY",
    ),
    AIMessage(
        content="The weather in San Francisco is currently 60 degrees and foggy.",
        response_metadata={
            "token_usage": {
                "completion_tokens": 15,
                "prompt_tokens": 143,
                "total_tokens": 158,
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": None,
            "finish_reason": "stop",
            "logprobs": None,
        },
        id="run-d15fcd86-3930-4736-a5b2-2f436bff0e6f-0",
        usage_metadata={"input_tokens": 143, "output_tokens": 15, "total_tokens": 158},
    ),
    HumanMessage(
        content="what is the weather in sf", id="e8769b13-b2cb-400a-9d9d-4f689069e287"
    ),
    AIMessage(
        content="",
        additional_kwargs={
            "tool_calls": [
                {
                    "id": "call_leMsdys8m5ZQ9jI1Mq5b8q2F",
                    "function": {
                        "arguments": '{"query": "weather in San Francisco"}',
                        "name": "search",
                    },
                    "type": "function",
                }
            ]
        },
        response_metadata={
            "token_usage": {
                "completion_tokens": 31,
                "prompt_tokens": 171,
                "total_tokens": 202,
            },
            "model_name": "gpt-3.5-turbo-0125",
            "system_fingerprint": None,
            "finish_reason": "tool_calls",
            "logprobs": None,
        },
        id="run-d0e98ded-265e-454b-955f-6f4b90d8fd66-0",
        tool_calls=[
            {
                "name": "search",
                "args": {"query": "weather in San Francisco"},
                "id": "call_leMsdys8m5ZQ9jI1Mq5b8q2F",
                "type": "tool_call",
            }
        ],
        usage_metadata={"input_tokens": 171, "output_tokens": 31, "total_tokens": 202},
    ),
    ToolMessage(
        content='["It\'s 60 degrees and foggy."]',
        name="search",
        id="4d95a516-b658-4447-b8f2-abd83e08ad7e",
        tool_call_id="call_leMsdys8m5ZQ9jI1Mq5b8q2F",
    ),
]
