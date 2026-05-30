import json
import random

def generate_video_prompt(base_description, kinks, num_variations=6):
    templates = [
        "Ultra photorealistic {duration} gay porn video clip, cinematic style, smooth motion, 4K: {base}. Extreme close-ups on {details}. Hyper-detailed male anatomy, glistening sweat, intense lust, natural outdoor lighting.",
        "High quality video generation prompt for {platform}: Muscular hairy stud in backyard {action}, {kink_details}. Massive cock focus with {cock_details}, raw {sex_act}. Maximum filth, dripping fluids, powerful thrusting.",
        "Photorealistic gay erotica video: {base} with extreme explicit action. {kink_list}. Visible veins, heavy balls slapping, precum and piss streams, breeding creampie finish."
    ]
    
    kink_descriptions = {
        'big_cocks': 'extremely thick veiny monster cock, girthy shaft throbbing',
        'blowjobs': 'deepthroat blowjob with bulging cheeks, spit dripping everywhere, gagging sounds',
        'anal': 'raw anal breeding, tight hole stretched wide, balls-deep pounding',
        'piss_play': 'powerful golden piss stream blasting on body and cock, golden shower fetish',
        'sweat_on_balls': 'sweat dripping down heavy low-hanging balls',
        'visible_precum': 'thick precum oozing from urethra and dripping down shaft',
        'heavy_foreskin': 'realistic heavy foreskin pulled back revealing sensitive glans',
        'throat_fucking': 'aggressive throat fucking with visible bulge in neck',
        'breeding': 'deep breeding creampie, cum leaking from stretched hole'
    }
    
    prompts = []
    for i in range(num_variations):
        base = base_description
        selected_kinks = random.sample(kinks, min(len(kinks), 5))
        kink_list = ', '.join([kink_descriptions.get(k, k) for k in selected_kinks])
        
        cock_details = kink_descriptions.get('big_cocks', '') + ', ' + kink_descriptions.get('heavy_foreskin', '')
        details = kink_list + ', sweat covered muscular bodies'
        
        prompt = templates[random.randint(0, len(templates)-1)].format(
            duration="8-12 second",
            base=base,
            details=details,
            platform=random.choice(["Grok", "Runway Gen-3", "Kling AI", "Luma Dream Machine", "Pika Labs"]),
            action="black speedo yanked down exposing massive cock",
            kink_details=kink_list,
            cock_details=cock_details,
            kink_list=kink_list,
            sex_act=random.choice(["throat fucking", "raw anal", "piss play while fucking"])
        )
        prompts.append(prompt)
    
    return prompts

# Run with user params
base_description = "muscular hairy stud against wooden fence, black speedo yanked down"
kinks = ['big_cocks', 'blowjobs', 'anal', 'piss_play', 'sweat_on_balls', 'visible_precum', 'heavy_foreskin', 'throat_fucking', 'breeding']

print("=== MAXIMUM FILTH GAY VIDEO PROMPTS ===")
prompts = generate_video_prompt(base_description, kinks, 6)
for i, p in enumerate(prompts, 1):
    print(f"\n**Video Prompt {i}:**")
    print(p)
    print("-" * 80)