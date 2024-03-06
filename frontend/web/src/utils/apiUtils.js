const BASE_URL = 'http://localhost';  

const fetchData = async (endpoint, port, options = {}) => {
  // const url = `${BASE_URL}:${port}/${endpoint}`;

  const url = "http://localhost:5001/flight_search"

  // Specify default headers, and allow them to be overridden
  const defaultHeaders = {
      'Content-Type': 'application/json' 
  };
  options.headers = {...defaultHeaders, ...options.headers};

  // Stringify the body if it's an object
  if (options.body && typeof options.body === 'object') { 
      options.body = JSON.stringify(options.body);
  }

  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error('API request failed');
  }

  return response.json();
};

export default fetchData;  