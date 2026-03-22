#!/usr/bin/env python3
"""
Milestone App Icon Generator
Creates app icons in all required sizes for iOS
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_milestone_icon(size):
    """Create a Milestone app icon with gradient background and calendar/clock symbol"""

    # Create image with gradient background
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)

    # Create gradient background (blue to purple)
    for y in range(size):
        # Gradient from #007AFF (iOS blue) to #5856D6 (iOS purple)
        r = int(0 + (88 - 0) * y / size)
        g = int(122 + (86 - 122) * y / size)
        b = int(255 + (214 - 255) * y / size)
        draw.rectangle([(0, y), (size, y+1)], fill=(r, g, b))

    # Draw rounded rectangle for calendar/card effect
    padding = size * 0.15
    card_left = padding
    card_top = padding
    card_right = size - padding
    card_bottom = size - padding
    corner_radius = size * 0.1

    # Draw white card with shadow effect
    shadow_offset = size * 0.02
    draw.rounded_rectangle(
        [(card_left + shadow_offset, card_top + shadow_offset),
         (card_right + shadow_offset, card_bottom + shadow_offset)],
        radius=corner_radius,
        fill=(0, 0, 0, 50)
    )

    draw.rounded_rectangle(
        [(card_left, card_top), (card_right, card_bottom)],
        radius=corner_radius,
        fill='white'
    )

    # Draw calendar header (colored bar at top)
    header_height = (card_bottom - card_top) * 0.25
    draw.rounded_rectangle(
        [(card_left, card_top), (card_right, card_top + header_height)],
        radius=corner_radius,
        fill=(0, 122, 255)
    )

    # Draw number (countdown style)
    number_size = int(size * 0.35)
    try:
        # Try to use system font
        font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", number_size)
    except:
        font = ImageFont.load_default()

    number_text = "7"

    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), number_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = (size - text_width) / 2
    text_y = card_top + header_height + (card_bottom - card_top - header_height - text_height) / 2

    draw.text((text_x, text_y), number_text, fill=(0, 122, 255), font=font)

    # Draw small "days" text below number
    days_size = int(size * 0.08)
    try:
        days_font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", days_size)
    except:
        days_font = ImageFont.load_default()

    days_text = "DAYS"
    days_bbox = draw.textbbox((0, 0), days_text, font=days_font)
    days_width = days_bbox[2] - days_bbox[0]
    days_x = (size - days_width) / 2
    days_y = text_y + text_height + size * 0.05

    draw.text((days_x, days_y), days_text, fill=(150, 150, 150), font=days_font)

    return img

def generate_all_icon_sizes(output_dir):
    """Generate all required iOS app icon sizes"""

    # iOS App Icon sizes (in pixels)
    sizes = {
        # iPhone
        'Icon-App-20x20@2x.png': 40,
        'Icon-App-20x20@3x.png': 60,
        'Icon-App-29x29@2x.png': 58,
        'Icon-App-29x29@3x.png': 87,
        'Icon-App-40x40@2x.png': 80,
        'Icon-App-40x40@3x.png': 120,
        'Icon-App-60x60@2x.png': 120,
        'Icon-App-60x60@3x.png': 180,

        # iPad
        'Icon-App-20x20@1x.png': 20,
        'Icon-App-29x29@1x.png': 29,
        'Icon-App-40x40@1x.png': 40,
        'Icon-App-76x76@1x.png': 76,
        'Icon-App-76x76@2x.png': 152,
        'Icon-App-83.5x83.5@2x.png': 167,

        # App Store
        'Icon-App-1024x1024@1x.png': 1024,
    }

    os.makedirs(output_dir, exist_ok=True)

    print("Generating Milestone app icons...")
    for filename, size in sizes.items():
        print(f"  Creating {filename} ({size}x{size})")
        icon = create_milestone_icon(size)
        icon.save(os.path.join(output_dir, filename))

    print(f"\n✅ All icons generated in: {output_dir}")
    print(f"📱 Total icons created: {len(sizes)}")

if __name__ == "__main__":
    output_dir = "/Users/toyball/Documents/WealthForge/projects/countdown-app/AppIcon.appiconset"
    generate_all_icon_sizes(output_dir)
