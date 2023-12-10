using Microsoft.Extensions.Configuration;
using Newtonsoft.Json.Linq;

var keyRing = new ConfigurationBuilder().AddJsonFile("appsettings.json");

string apiKey = configuration.;
int location = 1;


using (HttpClient client = new HttpClient())
{
    string urlAPI = $"https://api.openweathermap.org/data/2.5/weather?appid={apiKey}&id={location}";
    var json = JToken.Parse(urlAPI);

    Console.WriteLine(urlAPI);
}
