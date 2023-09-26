using System;
using System.Net.Http;
using System.Threading.Tasks;

public class CovidDataClient
{
    private readonly HttpClient _httpClient;

    public CovidDataClient()
    {
        _httpClient = new HttpClient();
    }

    public async Task<string> GetContinentsCovidDataAsync()
    {
        string url = "https://disease.sh/v3/covid-19/continents";
        HttpResponseMessage response = await _httpClient.GetAsync(url);

        if (response.IsSuccessStatusCode)
        {
            return await response.Content.ReadAsStringAsync();
        }
        else
        {
            throw new HttpRequestException("Falha na solicitação à API de Continents");
        }
    }

    public async Task<string> GetGlobalCovidDataAsync()
    {
        string url = "https://disease.sh/v3/covid-19/all";
        HttpResponseMessage response = await _httpClient.GetAsync(url);

        if (response.IsSuccessStatusCode)
        {
            return await response.Content.ReadAsStringAsync();
        }
        else
        {
            throw new HttpRequestException("Falha na solicitação à API disease.sh");
        }
    }

    public async Task<string> GetStateCovidDataAsync()
    {
        string url = "https://disease.sh/v3/covid-19/states";
        HttpResponseMessage response = await _httpClient.GetAsync(url);

        if (response.IsSuccessStatusCode)
        {
            return await response.Content.ReadAsStringAsync();
        }
        else
        {
            throw new HttpRequestException("Falha na solicitação à API de Estados");
        }
    }
}

class Program
{
    static async Task Main()
    {
        try
        {
            var covidClient = new CovidDataClient();
            string continentsData = await covidClient.GetContinentsCovidDataAsync();

            Console.WriteLine("Dados da COVID-19 por Continentes:");
            Console.WriteLine(continentsData);

            string globalData = await covidClient.GetGlobalCovidDataAsync();

            Console.WriteLine("Dados Globais da COVID-19:");
            Console.WriteLine(globalData);

            string stateData = await covidClient.GetStateCovidDataAsync();

            Console.WriteLine("Dados da COVID-19 por Estados:");
            Console.WriteLine(stateData);
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Erro na solicitação HTTP: {ex.Message}");
            if (ex.Message.Contains("Continents"))
            {
                Console.WriteLine("Erro na API de Continents");
            }
            else if (ex.Message.Contains("disease.sh"))
            {
                Console.WriteLine("Erro na API disease.sh");
            }
            else if (ex.Message.Contains("Estados"))
            {
                Console.WriteLine("Erro na API de Estados");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ocorreu um erro: {ex.Message}");
        }
    }
}


