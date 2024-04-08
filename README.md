# Data visualization for the evolution of Wikipedia articles maintained by WikiProjects

This project encompasses a web application designed to visualize time-series data related to Wikipedia's climate change articles, offering insights into content growth, interconnectedness, and information depth over time. The application utilizes a variety of technologies and structures, outlined as follows:

### **Backend Technologies**

- **Flask**: A lightweight WSGI web application framework used to build the backend. Flask serves as the cornerstone of the project, handling HTTP requests, routing, and serving the API endpoints that fetch and process data.
- **Pandas**: A powerful data manipulation and analysis library for Python, used to load, preprocess, filter, and aggregate the dataset from a CSV file. It's pivotal for handling the time-series data, enabling efficient operations like resampling and averaging over specific time intervals.
- **Matplotlib**: A comprehensive library for creating static, animated, and interactive visualizations in Python. It's utilized to generate plots based on the aggregated data, which are then returned as images to the client.
- **Python**: The primary programming language of the project, which ties together the use of Flask, Pandas, and Matplotlib. Python's versatility and the extensive ecosystem of data analysis and web development libraries make it an ideal choice for this project.

### **Frontend Technologies**

- **HTML**: Defines the structure of the web application's interface, containing the elements for user input (such as date pickers and feature selection dropdown) and displaying the generated visualizations.
- **CSS (Bootstrap)**: Used to style the webpage, leveraging Bootstrap, a front-end framework for developing responsive and mobile-first websites. It ensures the application is aesthetically pleasing and user-friendly across various devices.
- **JavaScript**: Facilitates dynamic interactions on the client side, such as capturing user inputs, making asynchronous requests to the Flask backend for data, and updating the webpage with new visualizations without needing to reload the page.

### **Data Structure and Handling**

- **CSV File**: The project's dataset is stored in a CSV file, which includes various metrics about Wikipedia articles on climate change over time. This format allows for easy data manipulation and analysis with Pandas.
- **Dataframe**: Within Pandas, the dataset is represented as a DataFrame, a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure. It's ideal for performing the necessary data preprocessing, filtering, and aggregation tasks.

### **Deployment and Operational Structure**

- **Docker** (optional for deployment): Can be used to containerize the application, encapsulating it along with its environment and dependencies. This ensures consistency across development, testing, and production environments.

### **Conclusion**

The project integrates various technologies and structures to facilitate the visualization of Wikipedia data related to climate change articles. It showcases the power of combining Python's data processing capabilities with Flask's simplicity for web development, along with client-side technologies for creating an interactive user experience.
