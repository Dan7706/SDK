using System;
using System.IO;
using System.Net;

public interface IOpenWeatherMapAPI
{
    string GetWeather(string city);
}

public class OpenWeatherMapSDK : IOpenWeatherMapAPI
{
    private string apiKey;

    public OpenWeatherMapSDK(string apiKey)
    {
        this.apiKey = apiKey;
    }

    public string GetWeather(string city)
    {
        string url = $"https://api.openweathermap.org/data/3.0/weather?q={city}&appid={apiKey}";

        try
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "GET";  //mentioning the request type

            using (WebResponse response = request.GetResponse())
            {
                using (Stream stream = response.GetResponseStream())
                {
                    StreamReader reader = new StreamReader(stream);
                    return reader.ReadToEnd();
                }
            }
        }
        catch (WebException ex)
        {
            using (WebResponse errorResponse = ex.Response)
            {
                HttpWebResponse httpResponse = (HttpWebResponse)errorResponse;
                Console.WriteLine($"Error: {httpResponse.StatusCode}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }

        return null;
    }

    public string AskForCity()
    {
        Console.Write("Enter the city for weather broadcast: ");
        return Console.ReadLine();
    }

    ~ OpenWeatherMapSDK ()
    { 
        //This is a destructor for OpenWeatherMapSDK class
        Console.WriteLine("OpenWeatherMapSDK instance deleted!")        
    }

    
    public static void Main(string[] args)
    {
        string apiKey = "YOUR_API_KEY";
        using (OpenWeatherMapSDK sdk = new OpenWeatherMapSDK(apiKey))
        {
            string city = sdk.AskForCity();
            string weatherData = sdk.GetWeather(city);
            Console.WriteLine(weatherData);
        }
    }
}

