from django.shortcuts import render
from datetime import date
postslist = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "mountains.jpg",
        "author" : "Ishaan Mavinkurve",
        "date": date(2025,7,6),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened while enjoying the view!",
        "content" : """
         The first light of dawn spilled over the peaks, painting the snow-capped mountains in hues of gold and rose. I stood at the edge of the trail, breathless—not from the climb, but from the view. The silence was immense, broken only by the distant rumble of a shifting glacier and the soft crunch of boots on frostbitten earth. It felt like standing on the edge of the world.

         The trek had been grueling. Each step tested my resolve, as thin air bit into my lungs and my legs threatened to give way. But there was a strange rhythm to it all—the slow, deliberate movement, the quiet camaraderie among fellow trekkers, the shared nods and glances that said, "We're still going." It reminded me that strength isn’t always loud.
         
         At night, we gathered around a small campfire, wrapped in wool and stories. The stars above were endless, impossibly bright, like someone had torn holes in the sky. I remember thinking how small we really are in the face of these ancient giants. But somehow, that smallness didn’t feel insignificant—it felt sacred.

         Reaching the summit wasn’t about conquering anything. It was about listening—truly listening—to the wind, the mountains, and myself. I left with sore legs and a quieter mind. The mountains had taken something heavy from me, and in return, they left a stillness I hadn’t known I was missing."""
    },
    {
        "slug": "lost-in-the-forest",
        "image": "woods.jpg",
        "author": "Ishaan Mavinkurve",
        "date": date(2025, 7, 3),
        "title": "A Walk Through the Wild",
        "excerpt": "I thought it would be a peaceful walk among the trees... until I realized I had no idea where I was.",
        "content": """
        The forest welcomed me with a hush, like it was holding its breath. Every step I took on the leaf-strewn path seemed louder than it should’ve been. The canopy above filtered the sunlight into flickers and shadows, and I felt like I had stepped into an entirely different world—one ruled by roots, moss, and memory.

        I kept walking, lulled by the rhythm of birdsong and the rustle of branches. But at some point, the path disappeared. I turned back and saw nothing familiar. My heartbeat quickened, but I kept calm. I had water, I had daylight, and somehow, I felt like the forest wasn’t trying to scare me—it just wanted me to pay attention.

        I followed a stream, hoping it would lead somewhere. And in that slow walk, I noticed things I hadn’t before—the deep green of ferns, the odd shape of a mushroom, the way sunlight shimmered on the water like glass. I wasn’t just walking through the forest anymore. I was in it, fully.
        Eventually, I stumbled back onto the trail. Relief washed over me, but a strange part of me missed the disorientation. Getting lost wasn’t the worst thing—it reminded me to slow down, to look, and to listen to the places we often rush through.
        """
    },
    {
        "slug": "desert-night-silence",
        "image": "desert.jpeg",
        "author": "Ishaan Mavinkurve",
        "date": date(2025, 6, 28),
        "title": "A Night in the Desert",
        "excerpt": "Deserts are supposed to be lifeless and still. But that night, something shifted inside me in the quiet sands.",
        "content": """
        As the sun dipped below the dunes, the desert turned cold fast—like someone had flipped a switch. The heat fled and silence settled in, thicker than anything I’d ever known. I wrapped myself in a blanket and sat on the sand, watching stars blink to life in the endless sky.

        There’s something about the desert at night. It's not just quiet—it’s a kind of holy hush, where even thoughts seem to whisper. I lay back and let the grains of sand cradle me, as if the earth itself was holding me still for once.

        The air was dry and sharp, carrying with it the scent of dust and distance. A jackal howled somewhere far off, and I felt more alive than I had in days. Out here, there was no signal, no noise, no rush—just me and the void, and strangely, it didn’t feel empty.
        I watched the moon rise, silver and ancient, over the dunes. I had come looking for silence, but what I found was presence. I left the desert with no answers, just a heart that felt a little less crowded.
        """
    }

]

def get_date(post):
    return post['date']

# Create your views here.


def  homePage(request):
    sorted_posts = sorted(postslist,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : postslist
    })

def singleBlog(request, slug):
    id_post = next(post for post in postslist if post['slug'] == slug)
    return render(request, "blog/singlepost.html", {
        "post" : id_post
    })