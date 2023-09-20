import UIKit

class ViewController: UIViewController {

    @IBOutlet var Temp: UILabel!
    @IBOutlet var Desp: UILabel!

    var todayTemperature: Int?

    override func viewDidLoad() {
        super.viewDidLoad()
        fetchTemperature() // Call the fetchTemperature function in viewDidLoad
    }

    func fetchTemperature() {
        let jsonURLString = "https://api.weather.gov/gridpoints/OKX/34,38/forecast"

        if let url = URL(string: jsonURLString) {
            let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
                if let error = error {
                    print("Error: \(error.localizedDescription)")
                    return
                }

                guard let data = data else {
                    print("No data received.")
                    return
                }

                do {
                    if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
                        print(json)
                        if let properties = json["properties"] as? [String: Any],
                           let periods = properties["periods"] as? [[String: Any]] {
                            if let firstPeriod = periods.first,
                               let temperature = firstPeriod["temperature"] as? Int {
                                self.todayTemperature = temperature

                                DispatchQueue.main.async {
                                    self.NYC()
                                }
                            }
                        }
                    }
                } catch {
                    print("Error parsing JSON: \(error.localizedDescription)")
                }
            }

            task.resume()
        }
    }

    @IBAction func NYC() {
        if let temperature = todayTemperature {
            Temp.text = "\(temperature)°F"
        } else {
            Temp.text = "N/A"
        }
    }

}
