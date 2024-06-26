# Blades in the Dark API

This project is an API for the game "Blades in the Dark". The API provides access to playbooks, abilities, and other game-related data. This API is made for [ZelenskaD](https://github.com/ZelenskaD) as a part of [Springboard](https://www.springboard.com/)'s Software Engineering Career Track Capstone Project 1.

## Features

- Access to all playbooks and their special abilities
- Access to all crews and their special abilities
- Access to all cohorts
- AI Image Generation for character creation
- Detailed Swagger API documentation
- CORS enabled for cross-origin requests

## Setup and Run

### Prerequisites

- Java 17
- sbt 1.8.1
- Scala 2.12.15

### Running the Application

1. **Compile the application:**

   ```
   $ sbt clean compile
   ```

2. **Run the application:**

   ```
   $ sbt run
   ```

3. **Access the API:**

    - **Swagger UI:** <https://blades-portal-api.surganov.dev/swagger>
    - **Swagger JSON:** <https://blades-portal-api.surganov.dev/api-docs/swagger.json>

## API Endpoints

### Playbooks
- **GET /api/playbooks**: Retrieve all playbooks
- **GET /api/playbooks/{name}**: Retrieve a specific playbook by name

### Crews
- **GET /api/crews**: Retrieve all crews
- **GET /api/crews/{name}**: Retrieve a specific crew by name

### Cohorts
- **GET /api/cohorts**: Retrieve all cohorts
- **GET /api/cohorts/{type}**: Retrieve a specific cohort by type

### AI
- **POST /api/ai/generate-character-image**: Generates a portrait for your character

## Documentation

The API documentation is provided using Swagger. You can access the Swagger UI at <https://blades-portal-api.surganov.dev/swagger>.

## Contact

For any issues or contributions, please visit the [GitHub repository](https://github.com/avsurganov/blades-portal-api) or contact [Vlad Surganov](https://www.linkedin.com/in/avsurganov/).

## License

This project is licensed under the Creative Commons Attribution 4.0 Unported License. See the [LICENSE](https://github.com/avsurganov/blade-portal-api?tab=CC-BY-4.0-1-ov-file#readme) file for details.
