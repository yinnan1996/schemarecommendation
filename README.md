# About The Project
This GitHub repository houses the implementation of the algorithms presented in our research paper "Semi-automatic construction of heterogeneous data schema based on structure and context-aware recommendation."   The paper is designed to implement a semi-automatic data schema construction system that facilitates the creation of customized data schemas in the field of materials science.    It leverages a structure and context-aware recommendation approach to enhance schema creation efficiency, reduce schema proliferation, and promote data sharing and collaboration among researchers.    The system is intended to be a valuable tool for data scientists, materials researchers, and anyone involved in the management and publication of scientific data.

For detailed instructions on using the system, please refer to the accompanying documentation and tutorial video "Semi-automatic Data Schema Construction System Tutorial," which provides a step-by-step guide on leveraging the system's capabilities for efficient data schema construction.

## Table of Contents

1. [Setup](#setup)
2. [API Documentation](#api-documentation)
3. [Running the Application](#running-the-application)
4. [Video](#video)

## Setup

To set up the application, follow these steps:

1. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## API Documentation

### Endpoint: `/api/example`

**Method:** `POST`

**Description:**
Calculates the similarity between input JSON data and data extracted from an Excel sheet and return the top N similar items.

**Request Body:**
```json
{
    "_ord": [
        "Magnetic Electronic Materials Category",
        "Material Information",
    ],
    "Magnetic Electronic Materials Category": {
        "r": true,
        "t": 1,
        "misc": {}
    },
    "Material Information": {
        "r": false,
        "t": 9,
        "misc": {
            "_ord": [
                "Chemical Formula",
                "Crystal Structure"
            ],
            "Chemical Formula": {
                "r": false,
                "t": 1,
                "misc": {}
            },
            "Crystal Structure": {
                "r": false,
                "t": 1,
                "misc": {}
            }
        }
    },
}
```

**Response:**
```json
[{
	"Preparation Process": {
		"misc": {
			"Preparation Techniques": {
				"misc": {},
				"r": false,
				"t": 1
			},
			"References": {
				"misc": {},
				"r": false,
				"t": 1
			},
			"Treatment Method": {
				"misc": {},
				"r": false,
				"t": 1
			},
			"_ord": ["Treatment Method", "Preparation Techniques", "References"]
		},
		"r": false,
		"t": 9
	},
	"_ord": ["Preparation Process"]
}, {
	"Preparation Parameters": {
		"misc": {
			"Pressure": {
				"misc": {
					"unit": "MPa"
				},
				"r": false,
				"t": 2
			},
			"Temperature": {
				"misc": {
					"unit": "K"
				},
				"r": false,
				"t": 2
			},
			"_ord": ["Pressure", "Temperature"]
		},
		"r": false,
		"t": 9
	},
	"_ord": ["Preparation Parameters"]
}, {
	"Electrical Transport": {
		"misc": {
			"Phase Diagram": {
				"misc": {
					"multi": false
				},
				"r": false,
				"t": 4
			},
			"Phase Transition Principle": {
				"misc": {},
				"r": false,
				"t": 1
			},
			"Phase Transition Temperature": {
				"misc": {
					"unit": "K"
				},
				"r": false,
				"t": 2
			},
			"_ord": ["Phase Transition Temperature", "Phase Transition Principle", "Phase Diagram"]
		},
		"r": false,
		"t": 9
	},
	"_ord": ["Electrical Transport"]
}]
```

**Success Response:**
- **Code:** 200
- **Content:** List of up to three data entries with the highest similarity scores.

## Running the Application

To run the application, use the following command:
```bash
python example_api.py
```

Once the server is running, you can access the API at `http://127.0.0.1:5000/api/example`.

Test.py demonstrates obtaining a response with an example. After launching the API application, use the following command to request the example API:
```bash
python test.py
```

## Video

Watch the tutorial video for the system via the link `https://youtu.be/V9gKsYhHvQA`

