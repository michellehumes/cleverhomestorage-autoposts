import os
import random
import requests
from datetime import datetime

# Configuration
WORDPRESS_SITE = os.environ.get('WORDPRESS_SITE', 'https://cleverhomestorage.com')
WORDPRESS_USERNAME = os.environ.get('WORDPRESS_USERNAME')
WORDPRESS_APP_PASSWORD = os.environ.get('WORDPRESS_APP_PASSWORD')
AMAZON_AFFILIATE_TAG = os.environ.get('AMAZON_AFFILIATE_TAG', 'cleverhomest-20')

# Room categories and related products
ROOMS = {
    'kitchen': {
        'title_templates': [
            '10 Kitchen Storage Hacks That Will Change Your Life',
            'The Ultimate Guide to Kitchen Organization in 2024',
            'Transform Your Kitchen: Best Storage Solutions',
            '15 Clever Kitchen Storage Ideas You Need to Try',
            'Kitchen Chaos? These Storage Tips Will Save You'
        ],
        'products': [
            {'name': 'SimpleHouseware Stackable Can Rack Organizer', 'asin': 'B01LXP8B6V'},
            {'name': 'Rev-A-Shelf Pull Out Cabinet Organizer', 'asin': 'B00MVMCFVU'},
            {'name': 'YouCopia ShelfSteps Cabinet Shelf', 'asin': 'B00MWQJVSO'},
            {'name': 'mDesign Lazy Susan Turntable', 'asin': 'B07CXZHS96'},
            {'name': 'Vtopmart Airtight Food Storage Containers', 'asin': 'B08NVQSR8M'}
        ]
    },
    'closet': {
        'title_templates': [
            'Maximize Your Closet Space: Expert Organization Tips',
            '12 Closet Storage Solutions for Small Spaces',
            'The Complete Closet Organization Guide for 2024',
            'Transform Your Closet with These Simple Hacks',
            'Professional Closet Organization Made Easy'
        ],
        'products': [
            {'name': 'ZOBER Velvet Hangers 50 Pack', 'asin': 'B01FOES65Y'},
            {'name': 'SimpleHouseware Closet Underwear Organizer', 'asin': 'B01FXDVVUG'},
            {'name': 'mDesign Fabric Storage Box Organizer', 'asin': 'B01MSRW0I4'},
            {'name': 'Whitmor Over The Door Shoe Rack', 'asin': 'B001F51AIS'},
            {'name': 'HOUSE DAY Space Saving Hangers', 'asin': 'B07HNKPQCG'}
        ]
    },
    'bathroom': {
        'title_templates': [
            'Bathroom Storage Ideas That Actually Work',
            '10 Genius Ways to Organize Your Bathroom',
            'Small Bathroom? Big Storage Solutions Here',
            'The Ultimate Bathroom Organization Guide',
            'Transform Your Bathroom with These Storage Hacks'
        ],
        'products': [
            {'name': 'mDesign Plastic Bathroom Storage Organizer', 'asin': 'B073P3ZH5R'},
            {'name': 'SimpleHuman Tension Shower Caddy', 'asin': 'B001P7RXLG'},
            {'name': 'DecoBros Wall Mount Organizer', 'asin': 'B01D58DR3G'},
            {'name': 'iDesign Linus Drawer Organizers', 'asin': 'B00PPVWXSO'},
            {'name': 'mDesign Metal Wire Wall Mount Towel Rack', 'asin': 'B0791W7SZV'}
        ]
    },
    'garage': {
        'title_templates': [
            'Garage Organization: From Chaos to Clarity',
            '15 Brilliant Garage Storage Solutions',
            'How to Maximize Your Garage Space in 2024',
            'The Complete Garage Organization System',
            'Transform Your Garage with These Storage Ideas'
        ],
        'products': [
            {'name': 'Rubbermaid FastTrack Garage Storage System', 'asin': 'B000PGTIUK'},
            {'name': 'FLEXIMOUNTS Overhead Garage Storage Rack', 'asin': 'B01N3JE3LU'},
            {'name': 'WallPeg Garage Tool Organizer', 'asin': 'B07F1ZYXPN'},
            {'name': 'Sterilite 18 Gallon Storage Tote', 'asin': 'B000MVYPV6'},
            {'name': 'Gladiator GearTrack Pack', 'asin': 'B001M0J8EG'}
        ]
    },
    'bedroom': {
        'title_templates': [
            'Bedroom Organization Tips for a Peaceful Space',
            '10 Under-Bed Storage Solutions You Need',
            'Create Your Dream Organized Bedroom',
            'Small Bedroom? Smart Storage Solutions Inside',
            'The Ultimate Bedroom Organization Guide'
        ],
        'products': [
            {'name': 'SONGMICS Under Bed Storage Containers', 'asin': 'B07RZQTB8W'},
            {'name': 'STORi Clear Plastic Drawer Organizers', 'asin': 'B07G387JDH'},
            {'name': 'mDesign Fabric Storage Box for Closet', 'asin': 'B0835VR65G'},
            {'name': 'Honey-Can-Do Hanging Closet Organizer', 'asin': 'B003ZBJIAQ'},
            {'name': 'Lifewit Storage Box with Lids', 'asin': 'B07MKCNBV2'}
        ]
    }
}

def generate_amazon_link(asin, tag):
    """Generate Amazon affiliate link"""
    return f"https://www.amazon.com/dp/{asin}?tag={tag}"

def generate_post_content(room, title, products):
    """Generate blog post content with product recommendations"""
    intro_templates = [
        f"Are you tired of the mess in your {room}? You're not alone! Today, I'm sharing my favorite storage solutions that have completely transformed my space.",
        f"Let's talk about {room} organization. If your {room} feels chaotic, these storage products will help you reclaim your space and your sanity.",
        f"Ready to transform your {room}? I've tested dozens of storage solutions, and these are the absolute best products that actually work.",
        f"Your {room} should be functional AND organized. Here are my top picks for storage solutions that will revolutionize your space."
    ]
    
    content = f"<p>{random.choice(intro_templates)}</p>\n\n"
    
    # Add product recommendations
    content += "<h2>My Top Storage Recommendations</h2>\n\n"
    
    for idx, product in enumerate(products[:5], 1):
        amazon_link = generate_amazon_link(product['asin'], AMAZON_AFFILIATE_TAG)
        content += f"""<h3>{idx}. {product['name']}</h3>
<p>This is one of my absolute favorites! The {product['name']} is a game-changer for {room} organization. It's durable, practical, and makes everything so much easier to find.</p>
<p><a href="{amazon_link}" target="_blank" rel="nofollow noopener">Check it out on Amazon →</a></p>\n\n"""
    
    # Add conclusion
    conclusions = [
        f"<p>These storage solutions have completely transformed my {room}. Which one are you most excited to try? Let me know in the comments!</p>",
        f"<p>Organization doesn't have to be overwhelming. Start with one of these products and watch your {room} transform!</p>",
        f"<p>Ready to get organized? Pick your favorite product from this list and get started today. Your future self will thank you!</p>"
    ]
    
    content += random.choice(conclusions)
    content += "\n\n<p><em>Note: This post contains affiliate links. If you purchase through these links, I may earn a small commission at no extra cost to you.</em></p>"
    
    return content

def publish_to_wordpress(title, content):
    """Publish post to WordPress via REST API"""
    url = f"{WORDPRESS_SITE}/wp-json/wp/v2/posts"
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    data = {
        'title': title,
        'content': content,
        'status': 'publish',
        'categories': [1]  # Adjust category ID as needed
    }
    
    response = requests.post(
        url,
        json=data,
        headers=headers,
        auth=(WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD),
        verify=False
    )
    
    if response.status_code == 201:
        post_data = response.json()
        print(f"✅ Post published successfully: {post_data['link']}")
        return True
    else:
        print(f"❌ Failed to publish post: {response.status_code}")
        print(f"Error: {response.text}")
        return False

def main():
    """Generate and publish a random blog post"""
    print("🚀 Starting blog post generation...")
    
    # Select random room
    room_name = random.choice(list(ROOMS.keys()))
    room_data = ROOMS[room_name]
    
    # Select random title
    title = random.choice(room_data['title_templates'])
    
    # Shuffle products for variety
    products = random.sample(room_data['products'], len(room_data['products']))
    
    print(f"📝 Generating post: {title}")
    print(f"🏠 Room: {room_name.capitalize()}")
    
    # Generate content
    content = generate_post_content(room_name, title, products)
    
    # Publish to WordPress
    success = publish_to_wordpress(title, content)
    
    if success:
        print("✨ All done! Post is live.")
    else:
        print("💥 Something went wrong. Check the logs.")

if __name__ == "__main__":
    main()
