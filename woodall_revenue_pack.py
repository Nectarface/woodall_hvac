import os
import json

# Configuration
TAILWIND = '<script src="https://cdn.tailwindcss.com"></script>'
FONTAWESOME = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'
NAV_LINKS = """
<a href="pricing.html" class="hover:text-blue-300 px-3 py-2 rounded-md font-medium">Pricing</a>
<a href="reviews.html" class="hover:text-blue-300 px-3 py-2 rounded-md font-medium">Reviews</a>
<a href="maintenance.html" class="hover:text-blue-300 px-3 py-2 rounded-md font-medium text-yellow-400"><i class="fa-solid fa-crown mr-1"></i> Club</a>
"""

def get_header(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Woodall Heating & Cooling</title>
    {TAILWIND}
    {FONTAWESOME}
</head>
<body class="bg-gray-50 text-gray-900 font-sans flex flex-col min-h-screen">
    <nav class="bg-blue-900 text-white sticky top-0 z-50 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <div class="flex items-center gap-3">
                    <a href="index.html" class="font-bold text-xl uppercase tracking-widest flex items-center gap-2">
                        <i class="fa-solid fa-snowflake text-blue-300"></i> Woodall
                    </a>
                </div>
                <div class="hidden md:flex space-x-6 items-center">
                    <a href="index.html" class="hover:text-blue-300 font-medium">Home</a>
                    <a href="services.html" class="hover:text-blue-300 font-medium">Services</a>
                    <a href="pricing.html" class="hover:text-blue-300 font-medium">Pricing</a>
                    <a href="reviews.html" class="hover:text-blue-300 font-medium">Reviews</a>
                    <a href="maintenance.html" class="text-yellow-400 font-bold border border-yellow-400 px-4 py-2 rounded hover:bg-yellow-400 hover:text-blue-900 transition">Join Club</a>
                    <a href="app/dashboard.html" class="bg-blue-800 px-4 py-2 rounded hover:bg-blue-700 text-sm">Tech Portal</a>
                </div>
            </div>
        </div>
    </nav>
    <main class="flex-grow">
"""

FOOTER = """
    </main>
    <footer class="bg-gray-900 text-white py-8 text-center border-t border-gray-800">
        <p>&copy; 2026 Woodall Heating & Cooling. Lebanon, IN.</p>
    </footer>
</body>
</html>
"""

FILES = {
    "pricing.html": {
        "title": "2026 HVAC Pricing Guide",
        "content": """
        <div class="max-w-4xl mx-auto px-4 py-12">
            <h1 class="text-4xl font-bold text-blue-900 mb-4">2026 HVAC Pricing Guide</h1>
            <p class="text-xl text-gray-600 mb-12">No secrets. Just honest numbers for Boone County homeowners.</p>
            
            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-red-600">
                    <h2 class="text-2xl font-bold mb-2">Furnace Install</h2>
                    <p class="text-4xl font-bold text-gray-900 mb-4">$4k - $7k</p>
                    <p class="text-gray-500 text-sm mb-6">Includes removal of old unit, new plenum, and 10-year warranty.</p>
                    <ul class="text-left space-y-2 mb-8 text-gray-700">
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> 80% to 96% Efficiency</li>
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> Smart Thermostat Included</li>
                    </ul>
                    <a href="app/seer_calc.html" class="block w-full text-center bg-red-600 text-white font-bold py-3 rounded hover:bg-red-700">Get Exact Quote</a>
                </div>

                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-blue-600">
                    <h2 class="text-2xl font-bold mb-2">AC Replacement</h2>
                    <p class="text-4xl font-bold text-gray-900 mb-4">$5k - $8k</p>
                    <p class="text-gray-500 text-sm mb-6">Full condenser and evaporator coil replacement.</p>
                    <ul class="text-left space-y-2 mb-8 text-gray-700">
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> 13 to 18 SEER2</li>
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> New Pad & Disconnect</li>
                    </ul>
                    <a href="app/seer_calc.html" class="block w-full text-center bg-blue-600 text-white font-bold py-3 rounded hover:bg-blue-700">Calculate Savings</a>
                </div>

                <div class="bg-white p-8 rounded-xl shadow-lg border-t-4 border-gray-600">
                    <h2 class="text-2xl font-bold mb-2">Repair & Tune-Up</h2>
                    <p class="text-4xl font-bold text-gray-900 mb-4">$89</p>
                    <p class="text-gray-500 text-sm mb-6">Standard diagnostic fee. Waived if you proceed with repair.</p>
                    <ul class="text-left space-y-2 mb-8 text-gray-700">
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> 21-Point Inspection</li>
                        <li><i class="fa-solid fa-check text-green-500 mr-2"></i> No Overtime Fees</li>
                    </ul>
                    <a href="contact.html" class="block w-full text-center bg-gray-800 text-white font-bold py-3 rounded hover:bg-gray-700">Book Service</a>
                </div>
            </div>
            
            <script type="application/ld+json">
            {
              "@context": "https://schema.org",
              "@type": "PriceSpecification",
              "price": "4000",
              "priceCurrency": "USD",
              "minPrice": "4000",
              "maxPrice": "7000",
              "description": "Furnace Installation Cost Lebanon IN"
            }
            </script>
        </div>
        """
    },
    "reviews.html": {
        "title": "Customer Reviews",
        "content": """
        <div class="max-w-2xl mx-auto px-4 py-16 text-center">
            <h1 class="text-4xl font-bold text-blue-900 mb-6">How did we do?</h1>
            <p class="text-xl text-gray-600 mb-12">Your honest feedback helps us keep Lebanon comfortable.</p>
            
            <div class="bg-white p-12 rounded-2xl shadow-2xl">
                <p class="font-bold text-gray-800 mb-6 text-lg">Rate your experience:</p>
                <div class="flex justify-center gap-4 text-5xl mb-8 cursor-pointer group">
                    <i class="fa-solid fa-star text-gray-300 hover:text-yellow-400 transition" onclick="rate(1)"></i>
                    <i class="fa-solid fa-star text-gray-300 hover:text-yellow-400 transition" onclick="rate(2)"></i>
                    <i class="fa-solid fa-star text-gray-300 hover:text-yellow-400 transition" onclick="rate(3)"></i>
                    <i class="fa-solid fa-star text-gray-300 hover:text-yellow-400 transition" onclick="rate(4)"></i>
                    <i class="fa-solid fa-star text-gray-300 hover:text-yellow-400 transition" onclick="rate(5)"></i>
                </div>
                
                <div id="feedback-form" class="hidden text-left mt-8 border-t pt-8">
                    <p class="text-red-600 font-bold mb-2">We're sorry we missed the mark.</p>
                    <p class="text-sm text-gray-600 mb-4">Please tell Mark (the owner) directly so he can fix it.</p>
                    <textarea class="w-full border p-3 rounded mb-4" placeholder="What happened?"></textarea>
                    <button class="bg-gray-900 text-white px-6 py-2 rounded">Send to Owner</button>
                </div>
            </div>
            
            <script>
                function rate(stars) {
                    if(stars >= 4) {
                        window.location.href = "https://google.com"; // Placeholder for G-Maps Link
                    } else {
                        document.getElementById('feedback-form').classList.remove('hidden');
                    }
                }
            </script>
        </div>
        """
    },
    "maintenance.html": {
        "title": "Comfort Club",
        "content": """
        <div class="max-w-5xl mx-auto px-4 py-16">
            <div class="bg-blue-900 rounded-3xl p-12 text-white text-center shadow-2xl relative overflow-hidden">
                <div class="relative z-10">
                    <div class="inline-block bg-yellow-400 text-blue-900 font-black px-4 py-1 rounded-full mb-6">MOST POPULAR</div>
                    <h1 class="text-5xl font-bold mb-6">The Woodall Comfort Club</h1>
                    <p class="text-2xl text-blue-200 mb-12">Total peace of mind for less than a pizza.</p>
                    
                    <div class="grid md:grid-cols-3 gap-8 text-left mb-12">
                        <div class="bg-blue-800 p-6 rounded-xl border border-blue-700">
                            <i class="fa-solid fa-bolt text-yellow-400 text-3xl mb-4"></i>
                            <h3 class="font-bold text-xl mb-2">Priority Status</h3>
                            <p class="text-blue-200 text-sm">You jump to the front of the line. Even during blizzards.</p>
                        </div>
                        <div class="bg-blue-800 p-6 rounded-xl border border-blue-700">
                            <i class="fa-solid fa-tags text-yellow-400 text-3xl mb-4"></i>
                            <h3 class="font-bold text-xl mb-2">15% Off Repairs</h3>
                            <p class="text-blue-200 text-sm">Save money on every part and every labor hour.</p>
                        </div>
                        <div class="bg-blue-800 p-6 rounded-xl border border-blue-700">
                            <i class="fa-solid fa-calendar-check text-yellow-400 text-3xl mb-4"></i>
                            <h3 class="font-bold text-xl mb-2">2 Free Tune-Ups</h3>
                            <p class="text-blue-200 text-sm">We clean your AC in spring and Furnace in fall. Automatically.</p>
                        </div>
                    </div>
                    
                    <button class="bg-yellow-400 text-blue-900 text-xl font-bold py-4 px-12 rounded-full hover:bg-white transition shadow-lg hover:scale-105 transform">
                        Join for $19/mo
                    </button>
                </div>
            </div>
        </div>
        """
    }
}

def generate_pack():
    for filename, data in FILES.items():
        full_html = get_header(data["title"]) + data["content"] + FOOTER
        with open(filename, "w") as f:
            f.write(full_html)
        print(f"[+] Generated {filename}")

if __name__ == "__main__":
    generate_pack()
    print("Revenue Pack Deployed.")
