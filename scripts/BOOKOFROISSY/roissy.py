from ebooklib import epub

# minimal metadata

book = epub.EpubBook()
book.set_identifier('258')
book.set_title('Core Game')
book.set_language('en')
book.add_author('Chateau Heartise')

book.set_cover("image.jpg", open('images.jpeg', 'rb').read())


# Chapters
# Introduction Chapter
intro = epub.EpubHtml(title='Introduction', file_name='intro.xhtml',
                      lang='en')

intro.content='<span><strong>The Roissy Reader: \
Chateau Heartiste on Game </strong></span> \
<br /> \
    <div id="pid_877175" style="padding: 5px 0 5px 0;">  \
                    “Heartiste is the intellectual linchpin of the \
Manosphere.” — <a href="http://www.rooshvforum.com/thread-36585-post-7437 \
87.html#pid743787" target="_blank">Frost</a><br /> \
                <br /> \
                “heartiste is the Aristotle of the manosphere.\
                His site is the bedrock of what people consider\
                common knowledge…” — <a href="http://www.rooshvf\
                orum.com/thread-36585-post-743125.html#pid743125"\
                target="_blank">MikeCF</a><br />\
                <br />\
                "There is no greater entry point for the curious\
                man,  no better archive,  no blog more skilled and\
                entertaining at truth telling,  nobody overlaps\
                the various worlds of truth better,  nobody\
                reduces the opposition to point and sputter\
                better than Heartiste.” — LaidNYC (now defunct)\
                <br />\
                <br />\
                “Heartiste is easily the biggest American\
                intellectual of the last 100 years or so,  and\
                has more impact on the lives of men than anyone\
                else.” — <a href="http://www.rooshvforum.com/post-\
                743165.html#pid743165" target="_blank">Samseau</a>\
                <br />\
                <br />\
                “8=====&gt;" — <a href="http://heartiste.wordpre\
                ss.com/2014/08/29/what-to-do-when-a-girl-scolds-\
                you/" target="_blank">Heartiste</a><br />\
                <br />\
                ##<br />\
                <br />\
                If you held a survey in this corner of the web\
                and asked guys their favorite game blog,\
                <a href="http://heartiste.wordpress.com/"\
                target="_blank">Heartiste</a> would win a\
                landslide. I''d definitely vote for him.<br />\
                <br />\
                There''s lots of good that can be said about\
                Heartiste—he''s an interesting stylist,  he has\
                an exceptional eye for detail,  he hasn''t\
                junked up his site with banner ads and popovers—\
                but\
                for my money,  what''s most appealing is that he\
                seems to genuinely love chasing and bedding women.\
                <br /> \
                <br /> \
                For whatever reason,  that''s not a given among\
                game bloggers,  even those who\
                (judging by their stories) are probably more\
                prolific in their snatch-getting than Heartiste.\
                But if I''m going to take my game cues from\
                somebody,  I''m not that interested in how many\
                girls he gets. I wanna know how much pleasure\
                he gets out of those girls,  and I think it''s\
                clear that for Heartiste,  the answer to\
                that question is "a lot."<br />\
                <br />\
'

# Foundation Chapter
foundations = epub.EpubHtml(title='Foundations', file_name='foundations.xhtml',
                            lang='en')
foundations.content='<span><strong>FOUNDATIONS</strong></span>'

# Endless Dating Chapter
f1 = epub.EpubHtml(title='Endless Dating', file_name='endless_dating.xhtml',
                            lang='en')
f1.content='<h2>Endless Dating</h2><p>How long is too long to stay in the \
dating game? The primary \
reason for the psychological unease and emotional instability of so many\
modern women and to a different extent modern men resides in the irresolvable\
tension between our ancient biological inheritance and the relatively recent\
emergence of the high-tech rootless world of unparalleled mate choice we now\
inhabit. </p>\
<p>It would shock most people if they were to be transported back in time\
to when humans lived in small tribes to see young girls having babies at\
14 and again at 14 years and 9.5 months.  There are subsistence cultures\
that behave this way today.  The bulk of our pre-history was spent in\
conditions like this so it is no wonder that our brains are having trouble\
coping with a radically different environment where childbirth is routinely\
put off until the mid-30s,  if at all,  and rejection by a woman no longer\
means banishment to the icy wastelands of celibate metadeath when a man need\
merely walk to the other side of a bar to try again.</p>\
<p>One consequence of this new paradigm is the absurd number of years spent\
in the dating circuit.</p>\
<p>Women are designed by nature to begin the next generation not much older\
than age 25.  Her risk of miscarriage or fetal abnormalities <a\
target="_blank" href="http://en.wikipedia.org/wiki/Fertility">increases</a>\
each year after that and exponentially so after 35.  Her body begins to\
wear down which affects how much energy she can devote to raising small\
children.  If she has not found a suitable mate by her late 20s she\
will begin to notice that those powerful feelings of infatuation she felt\
for crushes when she was younger,  perfectly created by evolution to bring\
a man and woman together to make babies,  now seem muted and foggy.  This\
in turn will sap the dating experience of the best things it has going\
for it &#8211; namely,  the spontaneity,  the euphoria,  the intense drive to\
connect &#8211; and leave behind a desiccated simulacra of dating that\
more closely resembles haggling over a business deal or suffering through\
a job interview.  Overthinking replaces lust.</p>\
<p>It is an embittering realization.</p>\
<p>Men,  too,  have had to adjust under the new system.\
Anthropologically-speaking,  it wasn&#8217;t so long ago that a man\
(or his immediate kin) blew his entire wad of hard-earned social and\
material capital wooing one or two women over the course of his\
natural lifespan.  In a pre-birth control age when the first\
deflowering blast inside a woman often meant conception followed by\
years of fatherhood there were limits on just how many female sex partners\
the average man could accumulate in a lifetime.  The rigorous experience\
of winning over and keeping the best quality woman he could afford and\
then providing for their kids soon thereafter meant that serial dating\
was not a typical feature of life.  Dating 40 or 50 different women in a\
year and jumping haphazardly in and out of 3-month mini-relationships is a\
peculiarity of modern life for which men are not optimized.  The energy\
requirement is enormous.  Men have adapted to this stressful cycle of\
meet-attract-close-keep by either settling and marrying the first girl that\
would have them (usually high school sweethearts who have not lived enough\
to acquire unrealistically picky standards) or by hardening themselves\
against the judgment of women and learning to play the numbers game.</p>\
<p>The game begat the player.</p>\
<p>In the gigantic atomized urban tribe of any big city playing the numbers\
is not the high risk strategy it once was for our distant male ancestors who\
were often locked out of any future matings when a pickup attempt went awry\
and the target or cockblock would run and tell the whole tribe what a loser\
he is.  Today,  the proximity of exes has very little impact on potential\
future conquests.  For men,  this has bought them virtually unlimited\
opportunity to get laid.  For women,  this has robbed them of one of their\
most potent weapons in ensuring that only the fittest males get access to\
their vaginas &#8212; the withering ostracization of their sexual rejection\
.</p>\
<p>On the flipside,  men have lost confidence in the fidelity of their\
chosen partners while women have gained unstigmatized sexual freedom\
allowing them to play the field until the perfect man finally arrives to\
sweep them off their feet.</p>\
<p>I do not think the current reality of endless dating can last.\
Something must give.  Either humans will evolve into different social\
animals capable of withstanding decades of hookups and fragmentary\
relationships without turning to the comforts of cats and internet porn,\
or those people who serially date and delay childbirth will not have enough\
kids and natural selection will remove them from the gene pool as a\
failed experiment.  Either way,  <a target="_blank"\
href="http://www.world-science.net/exclusives/070326_evolution.htm">change\
</a> is in the air.</p>'\

# The fundamental premise
f2 = epub.EpubHtml(title='The fundamental premise',
                   file_name='the_fundamental_premise',
                   lang='en')
f2.content ='<h2>The Fundamental Premise</h2>\
<p>Eggs are expensive, \
sperm is cheap. Every psychological\
dynamic you see playing out in mass societies liberated from artificial\
constraints on the sexual market flows from this premise. This means,\
as a systemic matter,  women are coddled,  men are upbraided. Women are\
victims,  men are victimizers. Women need a leg up,  men need to man up.\
Women have advocacy groups,  men have equal opportunity violations.\
A woman subjected to the indignity of eavesdropping on a tame joke about\
dongles makes national news,  while the chilling fact that 95% of all\
workplace deaths are suffered by men barely pings the media\
consciousness.</p>\
<p>It is what it is,  and it will never change so long as humans are a\
sexually reproducing species. All the laws in the world can at best\
only paper over the very primal compulsion of people to value the\
life of the average woman more than the life of the average man,\
and sympathize accordingly. Railing against it is akin to shaking a\
fist at sunspots and gamma rays. It&#8217;s therefore folly or\
self-serving disingenuousness to act like there’s some moral high\
ground to stake out by imparting culpable agency to an indifferent,\
organically emergent biomechanical phenomenon. Rationalizing favoritism\
toward women as some sort of payback for male privilege,  or refusing\
to acknowledge this favoritism altogether,  is an example of the\
cognitive calisthenics and evasive sophistry most people will indulge\
to avoid grappling with the cold,  black void of an uncaring evolutionary\
replication machine.</p>\
expendability was programmed into your wet code before you gained\
self-awareness. The worldscape of genes can rebuild with the seed of\
one man should catastrophe strike,  but each woman lost is a lethal\
blow to the repopulation project.</p>\
<p>In sober moments free of maudlin introspection,  you will understand\
there is no other game to play save this one. This is why to live as a\
man is to TAKE what you want. Not to wait for it to be given to you.\
Because it will never be given. Not to anticipate the empathy of the\
overseers. Because they will never empathize. Not to expect the coddling\
of the crowd. Because they will never coddle. Not to assume the wagon\
circling of kindreds. Because they will never circle for you. You got\
 he short stick,  now what? Do you contemplate it and hope for a\
longer one? No.</p>\
<p>You sharpen it and jab it into the heart of every obstacle that\
sets itself in your way.</p>'\

f3 = epub.EpubHtml(title='double standards',
                   file_name='double_standards.xhtml',
                   lang='en')
f3.content='<h2>Double Standards</h2><p>You hear it all the time from \
people who are getting\
shafted by reality.  &#8220;It&#8217;s so UNFAIR that guys get to do\
X with impunity while girls doing X suffer social stigma.&#8221;  They\
think by bitching like this and attempting to shame those who\
would live in harmony with double standards they can alter people&#8217;s\
behavior into something more to their liking (i.e.,  a non-status driven,\
non-materialistic,  non-craven utopia of perfect loving LTRs where no one\
left out and no one gets dumped and everyone\
as a soulmate and enough positive life-affirming experiences to share\
with their yenta friends in recipe-swapping blogs devoted to covering\
the fascinating minutiae of their funny,  exciting,  sexy,  touching, \
poignant,\
growth-oriented lives.)</p>\
<p>Then there are those who,  when called out\
on their inconsistencies,  deploy a swarm of sophistry intended to obfuscate\
and deny the existence of double standards because they are beneficiaries\
of them.  Acknowledging these truths would mean coming to terms with\
the fact that they,  like everyone else,  have at their core\
an animal nature.</p>\
<p>Fuck that noize.  The truth of the matter\
is that double standards are necessary if you want to be\
halfway competent in your dealings with men and women.  As the\
<a target="_blank" href="http://www.amazon.com/Winning-Through-Intimidation\
-Robert-Ringer/dp/0449207862/ref=sr_1_6/102-3180284-9010533?ie=UTF8&amp;s=\
books&amp;qid=1176423704&amp;sr=1-6">author</a> of &#8220;Looking Out for\
#1&#8221; and &#8220;Winning Through\
Intimidation&#8221; wrote:</p>\
<p>If you deny reality it will automatically work against\
you.*</p>\
<p>Double standards are fixed features of life as a sexually\
reproducing social organism.  The modern career woman is miserable because she\
is constantly locking horns with men who won&#8217;t value her for\
her career achievement as much as for her hourglass figure and\
bedroom skills,  while these same men admire and respect career dominance\
by other men.  Her refusal to come to grips with this\
essential double standard explains why so many hard-charging women have turned\
their backs on their own femininity and lost the art of\
female coquettishness and submissiveness.  Alpha men have responded by fucking\
and leaving these domineering gender impostors for cute waitresses.\
Betas have responded\
in their own way &#8212; by assuming the doormat position and\
giving these feminists *exactly* what they claim they want.</p> <p>The same\
goes for sluts.  A man who sleeps with many women gets\
high fives from his buddies and sexual interest from girls who\
can&#8217;t help their burning loins.  But girls who sleep around are\
socially ostracized,  used by men and shunned by women.  It has\
always been and it will always be as long as a\
woman has 400 eggs to a man&#8217;s nearly infinite number of\
sperm.  Parents will treat their sons and daughters differently \
when dispensing\
advice on how to deal with the opposite sex and all\
the harpies with their multiple humanities degrees shrieking equalist\
platitudes to\
the high heavens will never change this.  It&#8217;s one thing to\
bloviate from a comfy tenured perch while your lesbian lover sucks\
ben wa balls out of your cooch from under the desk;\
it&#8217;s quite another to entrust the welfare of your children with\
the twisted lies of the Bitterati.</p>\
<p>*pretty girls have some leeway\
with this rule. (at least for a while. heh.)</p>\
<p>A handy pocket guide to the most common double standards:</p>\
<p>male slut = lothario<br />\
female slut = desperate</p>\
<p>male CEO = alpha<br />\
female CEO = bitch</p>\
<p>male model = silly<br />\
female model = alpha</p>\
<p>male nerd = loser<br />\
female nerd = cute</p>\
<p>young male death = statistic<br />\
young female death = tragedy</p>\
<p>male nurse = beta<br />\
female nurse = agreeable</p>\
<p>male stripper = clown<br />\
female stripper = desirable</p>\
<p>male sports star = role model<br />\
female sports star = butch</p>'

f4 = epub.EpubHtml(title='latest baumeister paper support ch concept of the\
                   market',
                   file_name='latest_baumeister.xhtml',
                   lang='en')
f4.content="<h2>Latest Baumeister Paper Support CH Concept Of The Sexual\
Market</h2>"

f5 = epub.EpubHtml(title='this is your life',
                   file_name='this_is_your_life.xhtml',
                   lang='en')
f5.content='<h2>This Is Your Life</h2><p>Common American Man,\
this is how your life will unfold.\
You will start with dreams,  big dreams.  You will believe you are\
ordained for exceptionalism.  You will reluctantly abandon your dreams\
as the years pass and reality inexorably descends upon you like a choking\
shroud of grit.  That reality looks like this &#8212;</p>\
<p>You will get older,  uglier,  and fatter with each year.  Soon you will\
notice young women no longer take your flirtations seriously.  Your sloth\
and social detachment will worsen until people don&#8217;t even bother to\
be polite around you.  You will gradually lower your standards in what you\
want in a girl until desperation pushes you to marry a dumpy oinker well\
past her prime.  You will rut with her once a week,  then once a month,\
then holidays only.  You will relieve yourself drearily masturbating in the\
middle of the night by the cold flickering light of your computer monitor\
while that bloated seacow who doesn&#8217;t give a shit for your desires\
snores in the bed you can no longer get a good night&#8217;s sleep in.\
Your one shred of solace will come from knowing your depreciating asset\
(AKA wife) will have as few options as you do virtually guaranteeing lifelong\
fidelity.  Eventually you will have a couple of ungrateful snotty kids and\
your free time and discretionary cash will be completely obliterated.  You\
will squander whatever morsels of opportunity come your way as you settle into\
an achingly dull job paying the median wage dutifully punching the clock as a\
faceless cog in the corporate machine greasing the soul-soaked gears of the\
global marketplace with your bitter bloody tears.  You will silently mourn\
your impotent,  shriveled manhood as the established order extracts the last\
penny of tribute from your broken spirit.  You will numb the pain with alcohol\
,\
untold hours vegging in front of the TV,  and leveling your character in\
World of Warcraft.  Hours,  days,  months,  years will slip away.  Then,\
one lonely quiet cloudy day sitting in your well-worn easy chair,\
you&#8217;ll contemplate the arc of your life.  And you&#8217;ll feel\
the gnawing grip of emptiness as the crushing weight of what a barren\
nothingness your existence proved to be presses down on you.\
Barely comprehending,  you&#8217;ll shudder.  And then,  finally,  the\
Grim Reaper will steal your last breath and you will disappear from the\
world as if you had never been here and when they bury you no one will\
really notice and no one will really care because in your whole life you\
never never never,  not even once,  stepped off the hamster wheel and did\
anything courageous or interesting or different.</p>\
<p>And it will be too late when you realize that the chains clasped to\
your ankles and wrists were unlocked all along and you were always\
free to go.</p> <p align="center">~Fin~ </p>'\

f6 = epub.EpubHtml(title='arnie',
                   file_name='arnie.xhtml',
                   lang='en')
f6.content='<h2>Arnie</h2><p>Lex was a ruggedly handsome man,\
mid-40s,  and in shape\
from near daily yoga and martial arts classes. He was fidgety and frenetically\
hyperverbal and rarely came up for breath once he got rolling on a story\
drawn from his illustrious past and present lifestyle. And what stories! He\
ran a business in the recreation industry which put him in contact with a\
steady stream of young European girls. This contact often led to intimacy.\
Many patrons of his business would regale you with tales of \
witnessing Lex whisk\
some new 22 year old Polish hottie back to his quarters for a night\
of debauchery,  only to do it again the next night with a new\
girl.</p>\
<p>The four of us sat around the\
restaurant table swapping war stories from the field. Lex&#8217;s\
tomcat career was long and fruitful,  but an undercurrent of melancholic\
nostalgia buttressed\
the impression that he had let one or two &#8220;quality girls\
&#8221; get away. He seemed,  in a way,  a\
traitor to his contentment &#8212; a victim of chance and his compulsions\
. Lex made a passing comment,  barely noticed in the cavalcade of sex\
stories if you weren&#8217;t paying attention,  that &#8220\
;it was getting harder out there&#8221; and he needed to\
adjust accordingly.</p>\
<p><img data-attachment-id\
="2804" data-permalink="https://heartiste.wordpress.com\
/2009/04/16/arnie/img_2043b/" data-orig\
-file="https://heartiste.files.wordpress.com/2009\
/04/img_2043b.jpg?w=500&#038;h\
=375" data-orig-size="1600, 1200" data\
-comments-opened="1" data-image-meta="{&quot\
;aperture&quot;:&quot;2.8&quot;, &\
quot;credit&quot;:&quot;&quot;, &quot;camera\
&quot;:&quot;Canon PowerShot SD600&quot;, &quot;\
caption&quot;:&quot;&quot;, &quot;created_timestamp&quot\
;:&quot;1236464336&quot;, &quot;copyright&quot;:&\
quot;&quot;, &quot;focal_length&quot;:&quot;5\
.8&quot;, &quot;iso&quot;:&quot;\
0&quot;, &quot;shutter_speed&quot;:&quot;0\
.016666666666667&quot;, &quot;title&quot;:&quot;&\
quot;}" data-image-title="backstage at the met opera"\
data-image-description="" data-medium-file="https://\
heartiste.files.wordpress.com/2009/04/img_2043b.\
jpg?w=500&#038;h=375?w=\
300" data-large-file="https://heartiste.files.\
wordpress.com/2009/04/img_2043b.jpg?w=\
500&#038;h=375?w=500" class="\
size-full wp-image-2804 alignnone" title="backstage at\
the met opera" src="https://heartiste.files.wordpress.\
com/2009/04/img_2043b.jpg?w=500&#\
038;h=375" alt="backstage at the met opera"\
width="500" height="375" srcset="https://heartiste.\
files.wordpress.com/2009/04/img_2043b.jpg?\
w=500&amp;h=375 500w,  https://heartiste\
.files.wordpress.com/2009/04/img_2043b.jpg\
?w=1000&amp;h=750 1000w,  https://\
heartiste.files.wordpress.com/2009/04/img_2043b.\
jpg?w=150&amp;h=113 150w,  https\
://heartiste.files.wordpress.com/2009/04/img_2043b\
.jpg?w=300&amp;h=225 300w,\
https://heartiste.files.wordpress.com/2009/04/\
img_2043b.jpg?w=768&amp;h=576 768w\
" sizes="(max-width: 500px) 100vw,  500px" /></\
p>\
<p>Zeets admired the unapologetically masculine lifestyle Lex chose for\
himself. Marriage,  kids,  social approval,  clock punching and clock ticking\
? Fuck that noise. Lex lived on his own terms,  in hock\
to no one but himself. Zeets playfully encouraged Lex&#8217;s\
telling of his numerous conquests and the game he runs on women in the\
big city. Lex was especially fond of &#8220;fruit stand game\
&#8221; where he would casually sidle up to a girl (Lex\
banged chicks of all ages,  as long as they were younger than him\
) and guess what meal she was going to cook judging by the veggies\
she had in her basket. Since Lex was a competent cook,  this\
banter would often segue into him inviting her over for dinner.</p>\
\
<p>Trent,  the fourth and youngest man at the table,\
also approved of Lex&#8217;s playboy adventures,  but his approval\
carried more weight. Trent was a one woman kind of guy,  always\
strapped into a long term relationship that lasted for years and eager to get\
back into one on the rare occasions he was single. Trent was no\
herb; he had the tools and the skill to seduce many women if\
he wanted,  so his relatively monogamous existence was all the more \
intriguing.</\
p>\
<p>Outside of the restaurant we parted,  and Lex\
declined our offer to go to the bar for drinks and carousing. He\
was on his way back home to make a thousand calls. Lex could\
hardly focus on anything for long &#8212; his ADHD was legendary &#\
8212; and he barely stopped moving as we bro-slapped hands goodbye\
.</p>\
<p>Around 1AM back at Trent&#8217;\
s apartment,  as we were about to step inside,  an older man\
,  late 40s or early 50s,  with a paunch and one shirttail of\
his light blue button down poking out of his jeans,  greeted us with\
a weary but friendly expression. He introduced himself as Arnie and said he\
had been Trent&#8217;s neighbor for five years. Trent nodded\
his head knowingly as if he recognized Arnie,  but later told us in\
private he had never seen the guy. He probably had,  but it\
didn&#8217;t register.</p>\
<p>Arnie was\
an affable bloke,  and we stood outside in the mild air leaning against\
stair railings under the diffuse glow of the city lights for fifteen\
minutes talking\
guy stuff. We learned Arnie was never married,  lived alone,  and\
worked in a blue collar hands-on job,  and that it was\
clear to me that he possessed the basic intelligence to work white collar if\
he so chose. He had lived in the city his whole life and\
his apartment was rent controlled. There was no chance he would leave,\
despite the landlord working hard to force out his tenants by \
passively ignoring repairs\
that needed to be done.</p>\
<p>Arnie relished our\
company,  that much I could tell. He asked us if we were\
planning to go out somewhere again that night. Trent mentioned the bar where\
he bartended and Arnie made a frown,  explaining that that bar was too\
&#8220;hoity-toity&#8221; for him; he preferred\
down to earth establishments hanging &#8220;with the boys&#8221;.\
We laughed,  because Trent&#8217;s bar is not really snobby\
,  especially not for this city. We began turning our heads and shoulders\
toward the door and told Arnie we were going to call it a night\
. Arnie looked disappointed. &#8220;Well,  another time,  then\
.&#8221; He nodded at Trent. &#8220;Maybe I&#\
8217;ll meet you over at your bar sometime.&#8221; There\
was a hint of overeagerness in his gravelly voice.</p>\
<p\
>As we stepped inside to leave Arnie behind in the streetlight-misted\
night,  the door swung behind us with a slow creak. When it\
thumped closed,  it echoed heavily in my ears.</p>'

f7 = epub.EpubHtml(title='men with options',
                   file_name='men_with_options.xhtml',
                   lang='en')
f7.content='<h2>Men With Options</h2>'

f8 = epub.EpubHtml(title='what do women want? a master',
                   file_name='what_do_women_want_a_master.xhtml',
                   lang='en')
f8.content='<h2>What Women Want? A Master</h2><p>A reader asked if \
                   there were any books I could recommend that\
                   explored the psychology of women. I suggested &#8220;Story\
                   of O&#8221; and &#8220;9 1/2 Weeks&#8221;. (The latter\
                   was originally a book which is much better than the movie\
                   version.)</p>\
<p>There is a maxim among the pick-up community that if you want to know\
what women want it&#8217;s better to watch what they do than listen to what\
they say. Very true. However,  if you are going to listen to what a\
woman says for clues about her innermost desires,  or read what she\
writes,  you would do well to pay attention to what a woman says TURNS\
HER ON. Not what she says she wants in a hypothetical husband or boyfriend\
but what she specifically describes that got her horny and hungry for loving\
penetration. Any editorial commentary about the ideal man can be safely\
ignored.</p>\
<p>The two books above,  both written by women and featuring very beautiful\
female protagonists,  are wide-open windows to the id of women&#8217;s\
sexual natures. What we find there is shocking to most,  dispiriting to some,\
and unsurprising to a few. Women reading these books will, \
                   despite themselves,\
become uncomfortably aroused. Men will discover ancient stirrings within\
themselves they may have thought civilization and a PC academic indoctrination\
stamped out.</p> <p>The beatings and brandings the women in the books suffer,\
provoke,  and then eagerly anticipate in turn are distractions from the main\
message,  which is that the self-confidence and exquisitely suffocating\
domination of the male characters caused the women to fall so helplessly\
in love with them that the men could do anything,  make any demand,  and\
the women would happily go along just to keep their love. Some men can\
handle this awesome power,  some can&#8217;t. The man in 9 1/2 Weeks was\
consumed by his power as much as his lover,  and it got the better of\
him.</p>\
<p>These books,  taken together with the real world observations of men\
who actually live lives like those of the men in the books,  tell us what\
women want.</p>\
<p>They want a man who takes charge.</p>\
<p>A master.</p>\
    <p>Adopt the attitude of the master,  and women will revert to their\
    naturally submissive essence faster and more profoundly than you can\
    scarcely imagine,  and no amount of feminist propaganda,  insulating\
    credentials,  or careerist ladder climbing will stand in the way of\
    their joyous,  even relieving,  surrender to your intoxicating dominance\
    and confidence.</p>'

f9 = epub.EpubHtml(title='the ideal lover',
file_name='the_ideal_lover.xhtml',
lang='en')
f9.content='<h2>The Ideal Lover Can Never Be The Great Boyfriend</h2><p>\
Men are burdened with a duality. We feel impelled to commit to\
a chaste woman but we will happily sleep around with raging sluts. Women,\
too,  are creatures of duality. They relish the emotional connection with\
the great boyfriend who dotes on them and pampers them but they succumb\
helplessly to their raw sexuality with the ideal lover. The god of\
biomechanics is,  if nothing else,  a practical joker.</p>\
<p>There are very few men who embody both the great boyfriend and the ideal\
lover in equal measure. In fact,  my experience in the trenches of modern\
decadence leads me to conclude there are NO men like this. 50/50 internal\
power sharing between lover and supporter,  manifestly expressed in perfect\
synchronicity with a woman&#8217;s unspoken needs for the one or the other\
masculine archetype,  is the myth of &#8220;the One&#8221; perpetuated by\
the feminist grievance industry to keep women unsatisfied and constantly\
searching. The truth is that most men,  by innate character,  lean one way,\
and a few men of purity wholly abandon their soul&#8217;s struggle and\
jettison one archetype to fully embrace its opposite.</p>\
<p>How do you know if you are closer in character to the ideal lover or\
to the great boyfriend? To answer this for yourself,  consider the following\
scenarios,  and then decide if they accurately describe how you would behave\
in your own life.</p>\
<ul>\
<li>Holiday shopping (Kwanzaa not included)</li>\
</ul>\
<p>The great boyfriend thinks of the gifts he will buy others before he\
thinks of himself. His time shopping is spent with a gentle smile\
envisioning the look on his lover&#8217;s face when she sees what he\
bought for her.</p>\
<p>The ideal lover thinks of all the fantastic shit he will buy for\
himself before he thinks of others. His time shopping is spent with a\
joyous grin perusing the electronics section,  and only after he has\
sat in the massage chair at Brookstones for a while does he put in a\
token effort to find reasonably acceptable gifts for his girlfriend.</p>\
<ul>\
<li>Family</li>\
</ul>\
<p>The great boyfriend showers affection on his family. He is especially\
affectionate with little nieces and nephews.</p>\
<p>The ideal lover is either fighting or drinking with his family. He\
is the first to teach his little nephew how to flip the bird and what\
it means.</p>\
<ul>\
<li>Sex</li>\
</ul>\
<p>The great boyfriend is a master of foreplay and delaying his own\
gratification. He is a slow and steady lovemaker. The look of surrender on\
his woman&#8217;s face during orgasm brings him almost as much pleasure as\
his own climax. Sex is often preceded by the lighting of scented candles and\
the playing of soft jazz.</p>\
<p>The ideal lover is selfish in bed. He may eat his woman out for an\
eternity one night while hurting her anally another night,  slowly grind\
into her missionary style or jackhammer her like a rutting cape buffalo,\
but always know that everything he does sexually to her is in service to his\
penis. He will often not know nor care if she came,  and what usually precedes\
sex is a rough hand up her skirt.</p>\
<ul>\
<li>Compassion</li>\
</ul>\
<p>The great boyfriend will listen intently when his girl has had a bad day,\
careful not to brusquely offer any pointed suggestions to alleviate her\
sadness,  instead opting to massage her shoulders and make her some soup.</p>\
<p>The ideal lover will attempt to take his girl&#8217;s mind off her worries\
with hot sex. It will usually work.</p>\
<ul>\
<li>Values</li>\
</ul>\
<p>The great boyfriend appreciates his girlfriend&#8217;s values,\
and this is reflected in his mature respect for her political views,\
even when he disagrees.</p>\
<p>The ideal lover only cares for one value &#8212; his lover&#8217;s\
commitment to the righteousness of sexual abandon. He&#8217;s apolitical as\
far as she knows,  because he&#8217;s very good at mentally dismissing her\
silly political beliefs as the earnest naivete of an unworldly\
little girl.</p>\
<ul>\
<li>Compatibility</li>\
</ul>\
<p>The great boyfriend understands that much of what makes a relationship\
successful are shared goals and interests. He loves spending time with his\
lover doing things they both enjoy,  and he will put in the extra effort to\
learn about those things she likes to do but which he is either unfamiliar\
or uninterested. For instance,  if she likes tango dancing but he&#8217;d\
rather play pool,  he&#8217;ll spend a night or two attending tango\
classes with her and making her feel worth his sacrifice.</p>\
<p>The ideal lover understands that what makes a relationship successful is\
not spending too much time together. Quality over quantity,  and in his\
world the best measure of quality is how often intercourse is happening. He\
will occasionally treat his lover to romantic nights out,  but when she wants\
him to join her on <a href="https://heartiste.wordpress\
.com/2009/11/16/discovering-a-girls\
-soul-with-one-simple-question/" target="_blank\
">her trip to Antartica</a> he&#8217;ll stroke\
her cheek lovingly and tell her to have a good time by herself.</\
p>\
<p>These examples should give you an idea where on\
the testicular spectrum you fall. Are you a Latin lover or a loving\
partner? Like I said,  most men lean one way or the other\
,  a few embrace an extreme,  and only Master Casanovas balance their dual\
essence so evenly that their women are always breathlessly infatuated \
with them.</p\
>\
<p>The men who have <a href="https://\
heartiste.wordpress.com/2009/05/19/be-\
a-skittles-man/" target="_blank">complete command over their\
women</a> are the men who intuitively know when to disarm with\
the tender ministrations of the great boyfriend or the lustful\
recklessness of the ideal\
lover. When you are aware of this ever present immutable female desire for\
dualing male archetypes,  you will find it that much easier to direct a\
woman&#8217;s emotions,  like Mozart conducting a symphony. A\
woman&#8217;s loyalty is as much a function of your ability\
to seduce it out of her as it is of her character.</p>'

f10 = epub.EpubHtml(title='the sixteen commandments of poon',
file_name='the_sixteen_commandments_of_poon.xhtml',
lang='en')
f10.content='<h2>The Sixteen Commandments of Poon</h2><p><strong>I. Never\
say &#8216;I Love You&#8217; first</strong></p>\
<p>Women want to feel like they have to overcome obstacles to win\
a man&#8217;s heart. They crave the challenge of capturing the\
interest of a man who has other women competing for his attention,\
and eventually\
prevailing over his grudging reluctance to award his committed\
exclusivity. The man who gives\
his emotional world away too easily robs women of the\
satisfaction of earning his love\
. Though you may be in love with her,  don&#8217;t\
say it before she has said it. Show compassionate restraint for her need to\
struggle toward yin fulfillment. Inspire her to take the leap for you,  and\
she&#8217;ll return the favor a thousandfold.</p>\
<p\
><strong>II. Make her jealous</strong></p>\
<p\
>Flirt with other women in front of her. Do not dissuade other women\
from flirting with you. Women will never admit this but jealousy excites them.\
The thought of you turning on another woman will arouse her sexually. No girl\
wants a man that no other woman wants. The partner who harnesses the gale\
storm of jealousy controls the direction of the relationship.</p>\
<p><\
strong>III. You shall make your mission,  not your woman,  your\
priority</strong></p>\
<p>Forget all those romantic cliches of\
the leading man proclaiming his undying love for the woman who completes\
him. Despite\
whatever protestations to the contrary,  women do not want to be &#8220;\
The One&#8221; or the center of a man&#8217;s\
existence. They in fact want to subordinate themselves to a worthy man&#8217\
;s life purpose,  to help him achieve that purpose with their feminine support\
,  and to follow the path he lays out. You must respect a woman\
&#8217;s integrity and not lie to her that she is &#8220\
;your everything&#8221;. She is not your everything,  and if she\
is,  she will soon not be anymore.</p>\
<p><strong\
>IV. Don&#8217;t play by her rules</strong></\
p>\
<p>If you allow a woman to make the rules she\
will resent you with a seething contempt even a rapist cannot inspire.\
The strongest\
woman and the most strident feminist wants to be led by,  and to submit\
to,  a more powerful man. Polarity is the core of a healthy loving\
relationship. She does not want the prerogative to walk all over you with her\
capricious demands and mercurial moods. Her emotions are a hurricane,  her\
soul saboteur. Think of yourself as a bulwark against her tempest.\
When she grasps\
for a pillar to steady herself against the whipping winds or\
yearns for an authority\
figure to foil her worst instincts,  it is you who has to be there\
&#8230; strong,  solid,  unshakeable and immovable.</p>\
<p\
><strong>V. Adhere to the golden ratio</strong></p>\
\
<p>Give your woman 2/3 of everything she gives you.\
For every three calls or texts,  give her two back. Three declarations of\
love earn two in return. Three gifts; two nights out. Give her\
two displays of affection and stop until she has answered with three \
more. When\
she speaks,  you reply with fewer words. When she emotes,  you emote\
less. The idea behind the golden ratio is twofold &#8212; it establishes\
your greater value by making her chase you,  and it demonstrates that you have\
the self-restraint to avoid getting swept up in her personal dramas.\
Refraining\
from reciprocating everything she does for you in equal measure instills in\
her the proper\
attitude of belief in your higher status. In her deepest loins it is what\
she truly wants.</p>\
<p><strong>VI. Keep her\
guessing</strong></p>\
<p>True to their inscrutable natures,\
women ask questions they don&#8217;t really want direct answers to.\
Woe be the man who plays it straight &#8212; his fate is the\
suffering of the beta. Evade,  tease,  obfuscate. She thrives when she\
has to imagine what you&#8217;re thinking about her,  and withers\
when she knows exactly how you feel. A woman may want financial and family\
security,  but she does not want passion security. In the same manner,\
when she has displeased you,  punish swiftly,  but when she has done you\
right,  reward slowly. Reward her good behavior intermittently and\
unpredictably and she will\
never tire of working hard to please you.</p>\
<p><strong\
>VII. Always keep two in the kitty</strong></p>\
<\
p>Never allow yourself to be a &#8220;kept man&#8221\
;. A man with options is a man without need. It builds confidence and\
encourages boldness with women if there is another woman,  a safety net,  to\
catch you in case you slip and risk a breakup,  divorce,  or a\
lost prospect,  leading to loneliness and a grinding dry spell. A woman knows\
once she has slept with a man she has abdicated a measure of her power\
; when she has fallen in love with him she has surrendered nearly all of\
it. But love is ephemeral and with time she may rediscover her power and\
threaten to leave you. It is her final trump card. Withdrawing all her\
love and all her body in an instant will rend your soul if you are\
faced with contemplating the empty abyss alone. Knowing there is another\
you can turn\
to for affection will fortify your will and satisfy your manhood.</p>\
<\
p><strong>VIII. Say you&#8217;re sorry only when\
absolutely necessary</strong></p>\
<p>Do not say you&#\
8217;re sorry for every wrong thing you do. It is a posture\
of submission that no man should reflexively adopt,  no matter how alpha he is\
. Apologizing increases the demand for more apologies. She will come to\
expect your\
contrition,  like a cat expects its meal at a set time each day.\
And then your value will lower in her eyes. Instead,  if you have\
done something wrong,  you should acknowledge your guilt in a glancing\
way without resorting\
to the actual words &#8220;I&#8217;m sorry.&#8221\
; Pull the Bill Clinton maneuver and say &#8220;Mistakes were made&#\
8221; or tell her you &#8220;feel bad&#8221; about\
what you did. You are granted two freebie <em>&#8220;I\
&#8217;m sorry&#8221;</em>s for the life of\
your relationship; use them wisely.</p>\
<p><strong>IX\
. Connect with her emotions</strong></p>\
<p>Set yourself\
apart from other men and connect with a woman&#8217;s emotional landscape\
. Her mind is an alien world that requires deft navigation to\
reach your rendevous\
. Frolic in the surf of emotions rather than the arid desert of logic.\
Be playful. Employ all your senses. Describe in lush detail scenarios to set\
her heart afire. Give your feelings freedom to roam. ROAM. Yes,\
that is a good word. You&#8217;re not on a linear\
path with her. You are ROAMING all over,  taking her on an adventure\
. In this world,  there is no need to finish thoughts or draw conclusions\
. There is only need to EXPERIENCE. You&#8217;re grabbing her\
hand and running with her down an infinite,  labyrinthine alleyway\
with no end,\
laughing and letting your fingers glide on the cobblestone walls along\
the way.</p\
>\
<p><strong>X. Ignore her beauty</strong></p\
>\
<p>The man who trains his mind to subdue the reward centers\
of his brain when reflecting upon a beautiful female face will\
magically transform his interactions\
with women. His apprehension and self-consciousness will melt away,\
paving the\
path for more honest and self-possessed interactions with the\
objects of his desire\
. This is one reason why the greatest lotharios drown in more love than they\
can handle &#8212; through positive experiences with so many beautiful\
women they lose\
their awe of beauty and,  in turn,  their powerlessness under its spell.\
It will help you acquire the right frame of mind to stop using the words\
<em>hot,  cute,  gorgeous,  </em>or <em\
>beautiful </em>to describe girls who turn you on. Instead,\
say to yourself &#8220;she&#8217;s interesting&#8221;\
or &#8220;she might be worth getting to know&#8221;. Never\
compliment a girl on her looks,  especially not a girl you aren&#8217\
;t fucking. Turn off that part of your brain that wants to put\
them on pedestals. Further advanced training to reach this state of\
unawed Zen transcendence\
is to sleep with many MANY attractive women (try to avoid sleeping with a\
lot of ugly women if\
you don&#8217;t want to regress\
). Soon,  a Jedi lover you will be.</p>\
<p\
><strong>XI.  Be irrationally self-confident</strong></p>\
\
<p>No matter what your station in life,  stride through the world\
without apology or excuse. It does not matter if objectively you are not the\
best man a woman can get; what matters is that you think and act\
like you are. Women have a dog&#8217;s instinct for uncovering\
weakness in men; don&#8217;t make it easy for them.\
Self-confidence,  warranted or not,  triggers submissive emotional\
responses in women.\
Irrational self-confidence will get you more pussy than\
rational defeatism.</p>\
\
<p><strong>XII.  Maximize your strengths,  minimize your weaknesses</\
strong></p>\
<p>In the betterment of ourselves as men we\
attract women into our orbit. To accomplish this gravitational pull as\
painlessly and efficiently\
as possible,  you must identify your natural talents and shortcomings and\
parcel your efforts\
accordingly. If you are a gifted jokester,  don&#8217;t waste\
time and energy trying to raise your status in philosophical debate.\
If you write\
well but dance poorly,  don&#8217;t kill yourself trying to expand\
your manly influence on the dancefloor. Your goal should be to\
attract women effortlessly\
,  so play to your strengths no matter what they are; there is a\
groupie for every male endeavor. Except World of Warcraft.</p>\
<p\
><strong>XIII. Err on the side of too much boldness,  rather\
than too little</strong></p>\
<p>Touching a woman inappropriately\
on the first date will get you further with her than not touching her at\
all. Don&#8217;t let a woman&#8217;s faux\
indignation at your boldness sway you; they secretly love it when a\
man aggressively\
pursues what he wants and makes his sexual intentions known. You don&#8217\
;t have to be an asshole,  but if you have no choice,\
being an inconsiderate asshole beats being a polite beta,  every time.</p>\
\
<p><strong>XIV. Fuck her good</strong></p>\
\
<p>Fuck her like it&#8217;s your last fuck.\
And hers. Fuck her so good,  so hard,  so wantonly,  so\
profligately that she is left a quivering,  sparking mass of shaking\
flesh and sex\
fluids. Drain her of everything,  then drain her some more. Kiss her\
all over,  make love to her all night,  and hold her close in\
the morning. Own her body,  own her gratitude,  own her love.\
If you don&#8217;t know how,  learn to give her squirting\
orgasms.</p>\
<p><strong>XV. Maintain your state control\
</strong></p>\
<p>You are an oak tree. You will not be manipulated by\
crying,  yelling,  lying,  head games,  sexual withdrawal,  jealousy ploys,\
pity plays,  shit tests,  hot/cold/hot/cold,  disappearing\
acts,  or guilt trips. She will rain and thunder all around you and\
you will shelter her until her storm passes. She will not drag you into\
her chaos or uproot you. When you have mastery over yourself,  you will\
have mastery over her.</p>\
<p><strong>XVI.  Never be afraid to lose her</strong></p>\
<p>You must not fear. Fear is the love-killer.\
Fear is the ego-triumph that brings abject loneliness. You will face your\
fear. You will permit it to pass over and through you. And when\
your ego-fear is gone you will turn and face your lover,  and\
only your heart will remain. You will walk away from her when she has\
violated your integrity,  and you will let her walk when her heart is closed\
to you. She who can destroy you,  controls you. Don&#8217\
;t give her that power over yourself. Love yourself before you love her.</p>\
<p>***</p>\
<p>The closer you follow the letter of these commandments,  the easier\
you will find and keep real,  true unconditional love and happiness in\
your life\
.</p>\
<p>Best.</p>'

f11 = epub.EpubHtml(title='the fundamentals',
file_name='the_fundamentals.xhtml',
lang='en')
f11.content='<h2>The Fundamentals</h2><p>There is so much pickup information\
available now that\
it&#8217;s easy to lose sight of the fundamentals that govern sexual\
tension and attraction between men and women. When the information\
cascade overwhelms it begins to pull you away from what works,  and\
what has always worked for you\
. Consequently,  over-analysis can hinder your spiritual growth as\
a womanizer.\
That is why it is vital to step back every so often,  ignore the\
steady stream of advice,  and return to a few golden,  immutable laws of\
attraction that will never go out of style.</p>\
<p>The\
one fundamental to which I always return,  and has never failed to reward me\
as expected,  is this:</p>\
<p>Women cannot resist the\
aloof and indifferent man.</p>\
<p>Of all the compulsions hard\
-wired in a female&#8217;s hindbrain,  this one is etched\
deeper and more enduringly. Every woman,  to a greater or lesser degree,\
feels the burn of lust and the agony of love for a man who projects\
a &#8220;take it or leave it&#8221; attitude.</p\
>\
<p>Note that aloof and indifferent doesn&#8217;t mean\
haughty,  distant or uninterested. It means <em>disinterested.</em>\
It means that while you may love her and flatter her and soothe her and\
give her gifts,  underlying it all is an attitude that tells her &#8220\
;I can walk if necessary,  and find someone new.&#8221;</p\
>\
<p>It may seem counterproductive for a woman to respond so favorably\
to a man exhibiting this attitude,  but the evolution of human sociosexuality\
offers an\
explanation: an aloof man is indirectly advertising his skill at seducing\
women. Such\
a man will give a woman sons who will inherit his ladykiller genes. Conversely\
,  a man who gloms onto a woman may as well be holding a placard\
that says &#8220;My celibacy is nigh!&#8221;. He has no\
confidence that should his girlfriend or wife misbehave,  or leave him,\
he will\
be able to find another woman&#8217;s bossom for comfort.</p\
>\
<p>And really,  that&#8217;s what all this\
talk by women about valuing &#8220;confidence&#8221; in men means\
; what women are really saying is that they value men who could dump them\
on a whim and get with new women easily. Men who can do this\
are filled with the kind of confidence that turns women on.</p>\
<\
p>The aloof and indifferent attitude can be expressed reactively or\
proactively,  deliberately\
or passively. She senses it when other women flirt with you and you refuse\
to act ashamed for it. You don&#8217;t rub your desirability\
to competitor women in her face,  but neither do you downplay it.</p\
>\
<p>She senses it when she is the first to say &#\
8220;I love you&#8221;,  after many months of eager &#8212\
; but ultimately unfulfilled &#8212; anticipation on her part for you to say\
it first.</p>\
<p>She senses it when you occasionally pepper\
your relationship with unexplained absences.</p>\
<p>She senses it when\
you hang out with guy friends who are known players.</p>\
<p\
>She senses it when you drag your feet about going on expensive trips together\
.</p>\
<p>She senses it when you are <a href\
="https://heartiste.wordpress.com/2010/07/16/\
why-you-should-leave-after-sex/" target="_blank\
">the first to hop out of bed</a> after climax.</p\
>\
<p>She senses it when your exes are always bumping into you\
.</p>\
<p>She senses it when you announce that you don\
&#8217;t understand guys like her male friend who can only play video\
games when his girlfriend is not around to castigate him,  and when you then\
proudly and defiantly proclaim you value your &#8220;freedom and\
independence&#8221\
; too much to be like that guy.</p>\
<p>She senses it when a half-assed microwaved meal that you cooked for the\
both of you means more to her than a four course dinner\
slaved over for hours in the kitchen by a beta would mean to her.</\
p>\
<p>She senses it when you set the bar so low\
,  it becomes a challenge to disappoint her.</p>\
<p>The\
fundamentals. Be aloof. Be indifferent. Be loving.</p>\
<p\
>Do these three things and you will never be lacking for a woman&#\
8217;s eternally grateful love.</p>'

f12 = epub.EpubHtml(
    title='flattering words',
file_name='flattering_words.xhtml',
lang='en ')

f12.content='<h2>The Most Flattering Words You Can Hear From A Woman \
<p>Some of you naive souls may be thinking,  &#8220;\
Oh,  I know the answer! Me! Me! Look over here!&#\
8230;. &#8216;I love you&#8217;. Did I win?&#\
8221;</p>\
<p>No,  you did not. You LOSE\
,  madam. You get NOTHING. Good day to you.</p>\
<\
p>The answer is this: &#8220;How can you be such\
a jerk and so lovable at the same time?&#8221;</p>\
<\
p>Gentlemen,  if you hear that from a woman,  particularly a girlfriend\
or wife,  you will know you have penetrated her heart and mind to the\
soft,  chewy center of her hamster&#8217;s id,  which is\
one id level deeper than her own human id. You cannot possibly hear anything\
more flattering from a woman unless it&#8217;s a breathless demand to\
scour her cervical wall with your proud protuberance.</p>\
<p>&#8220\
;How is being called a jerk more flattering than just being\
called lovable?&#\
8221;</p>\
<p>Oh,  you silly,  anatomically ambiguous acculturated\
automaton. Don&#8217;t you know how to read girlcode? It\
&#8217;s like hieroglyphics,  except less understandable to the average man.\
When a girl calls you a jerk,  you have enflamed her vagina. When\
a girl calls you lovable,  you have palpitated her heart. When a girl\
calls you a jerk AND lovable,  you have made a slave of her.\
Recline in the pillow-soft comfort of your testicular allure,\
because from that\
point forward you can do no wrong.</p>'

f13 = epub.EpubHtml(title='love',
file_name='love.xhtml',
lang='en')
f13.content='<h2>Love</h2>'

c = epub.EpubHtml(title='chicks: their ways and workings',
file_name='chicks.xhtml',
lang='en')
c.content='<h2>Chicks: Their Ways and Workings</h2>'


c1 = epub.EpubHtml(title='where guys falter',
file_name='where_guys_falter.xhtml',
lang='en')
c1.content='<h2>Where Guys Falter</h2>\
<p>The best way to do well with women over the long haul\
is to think like them,  understand them,  and put yourself in their shoes\
.  The man who can empathize with a woman&#8217;s frustrations will\
know better how to make her happy.  All the great seducers of history co\
-opted to some degree the psychology and the courting tactics of women.  They\
used women&#8217;s pyschological weapons against them.</p>\
<p\
>This is why European men have a reputation for smoothness with the ladies &#\
8212; they spend more time than American men in the company of women,\
participating in activities and intellectual pursuits that appeal to women,\
learning about them.\
American men bemoan their dating hardships,  but spending all their free time\
watching sports\
,  drinking beer,  video gaming,  and golfing,  where no women are present\
,  only to take a flailing Saturday night stab at getting laid in overheated\
bar\
environments,  is not a good way to learn how to turn women on.</\
p>\
<p>The inexperience of many guys around women shows in their\
ham-fisted come-ons.  They often act so counter-productively that\
it&#8217;s a wonder any girls give it up to them at\
all.  Verbally gang tackling a group of girls at a bar is one example\
.  Which guy,  in a moment of reflection,  really believes that\
approaching two\
girls with five of his buddies in phalanx formation and swarming them\
like vultures over a carcass will win their affections?  Guys who\
don&#8217;t have\
the sack to approach women on their own should not advertise their weakness\
by storming\
in with a giant cock posse for battlefield support.  Two guys maximum.  If\
necessary,  hold off on waving the rest of the crew in until after the\
set has been warmed up in a non-threatening way.</p>\
<\
p>Guys also do not listen.  Well,  not in the way that\
women want to be listened to.  A guy should listen to a woman with\
the same intensity he listens to his buddies talk about football or\
German hookers.\
The focus that a nerd brings to tackling a coding problem is the same focus\
that a guy should have when listening to an attractive woman speak.  The trick\
is to do it with the distracted aloofness of someone not hanging on her every\
word.  It&#8217;s very alluring to a girl when a guy\
off-handedly recalls some inconspicuous detail he picked up about\
her while she was\
talking without looking like he worked hard to remember it.  It\
subconsciously says to\
her &#8220;This guy is not desperate,  but wow I must be\
making an impression because he remembers how I felt when I danced \
at my sister\
&#8217;s wedding.  We connect!&#8221;</p>\
<p\
>This isn&#8217;t meant as mealy-mouthed John Gray relationship\
pap; listening intently to a woman will give him all the information he needs\
to successfully seduce her.  Women reveal so much about themselves in\
conversation &#8212\
; they can&#8217;t help it because they are self-obsessed\
creatures by nature &#8212; but they only do it in subtle read-\
between-the-lines ways,  feminine ways,  that to the uninitiated man will pass\
right under his radar.  It&#8217;s a double curse\
that boobs and pretty eyes cloud his efforts to stay engaged with her words.</\
p>\
<p>To seduce women,  you must seduce yourself first.\
You are the guy who will be everything she needs.  How will you know\
what she needs?  Get inside her head.  Become her.</p>\
'


c2 = epub.EpubHtml(title='away from the comapny of women',
file_name='away_from_the_company_of_women.xhtml',
lang='en')
c2.content='<p><em>I am never in the company of men after 5.<br />\
</em>&#8211; Bertrand Morane</p>\
<p><em>After sex,  the company of women can be a drag.<br />\
</em>&#8211; Me</p>\
<p>I spend a lot of time with women. Either seducing them\
,  fucking them,  <a href="https://heartiste.wordpress.com\
/2009/06/04/is-lady-rain-in-\
this-porno/" target="_blank">fucking with them</a>,  listening \
to them,  scratching the napes of their necks,  or examining them like a \
disassembled timepiece. The purpose of such mingling goes deeper than \
enjoying the pleasure of \
their company. Books,  mentors,  a willingness to discard delusion and lies,  \
and a keen eye will aid a man in his divine quest to acquire as \
much sex and love as he can handle from beautiful women,  but no impetus \
to personal growth is as effective as direct interaction with the subject. \
Whether sex \
is or is not the goal,  being around women sharply flattens the learning curve\
. There may be a gene yet discovered which grants its possessor the \
innate ability \
to know how a woman ticks,  but if there is such a gene,  \
it is a neural algorithm that quickly decays from disuse. Even the \
best naturals \
had to <span style="text-decoration:line-through;">buck \
up and endure</span> spend glorious time around women before their Asmodeus-\
blessed gifts could find full expression.</p>\
<p>Given this reality\
,  some men might make the understandable mistake that their every \
waking moment should be \
with women or,  if no women are physically present,  with women in their \
thoughts. This would be a false extrapolation. Like a diligent \
scientist deep in \
the bowels of his flourescently dismal lab who has forgotten the \
feeling of the sun \
on his face,  a man who spends all his free time with women risks \
degeneration of his masculine core. Inhalation of the estrogenic fumes \
of too much distaff \
attention and his spirit becomes arthritic,  his testicular acuity \
blurs into maudlin mush. \
Perspective is lost.</p>\
<p>Men would do well to occasionally \
distance themselves from women and their petty intrigues,  and the best \
way to do \
this is not through solitude but in the company of other men,  reveling in \
hearty chest thumps,  metaphorical or real,  and swearing bloodstirring oaths \
to doctrines good \
and great that elude the grasp of women stuck in the mud of their uninspiring\
,  earthy practicality. And men,  unlike women,  are capable of their high \
drama without uttering a word.</p>\
<p>Let me cut to the chase: Women are mostly \
boring. Even,  maybe especially,  the brightest and most overeducated \
among them can \
induce cataract-like glazing of the eyes if given enough comfort and \
a sympathetic \
ear to unleash the menstrual force of their vaggy stream of consciousness. \
Disconnected from \
their bodies and sexuality,  their flirtations and flattery,  and their \
charm and whimsy\
,  women are incapable of seriously entertaining for any length of time \
greater than the \
duration from leer to spent urge any but the most desperately cloying of men. \
Sure there are exceptions &#8212; women of particularly engaging personalities \
and surprising fondness \
for the abstract &#8212; but these exceptions serve merely to remind a man \
of the depressing drabness of the mass of women with their meager,  \
provincial concerns\
.</p>\
<p>Don&#8217;t lose contact with the world of men\
. Their vigorous,  purposeful company is a refreshing tonic to the \
pedestrian prattle,  \
contrived machinations,  and histrionic solipsism of women.</p>\
'

c4 = epub.EpubHtml(title='the most misogynistic blog post \
                   on the internet',
file_name='misogynistic.xhtml',
lang='en')
c4.content='<h2>The Most Misogynistic Blog Post On The Internet</h2>\
<p>If people are going to accuse you of misogyny,  may as well enjoy the \
egotistic benefits of being a truth-telling misogynist.</p>\
<p>***</p>\
<p>Men move the discussion forward. Women swap recipes and beauty tips.</p>\
<p>Men debate. Women wheedle.</p>\
<p>Men confront. Women slander.</p>\
<p>Men act. Women plot.</p>\
<p>Men invent. Women benefit.</p>\
<p>Men are passionate. Women are passion parasites.</p>\
<p>Men cheat. Women betray.</p>\
<p>Men withdraw. Women shit test.</p>\
<p>Men kill. Women play let&#8217;s you and him fight.</p>\
<p>Men are emotionally distant. Women are emotionally manipulative.</p>\
<p>Men&#8217;s Achilles&#8217; heel is pride. Women&#8217;s Achilles&#8217; \
heel is vanity.</p>\
<p>Men die younger. Women live slower.</p>\
<p>Men think loftily. Women think grubbily.</p>\
<p>Men are expendable. Women are perishable.</p>\
<p>Men humiliate. Women shame.</p>\
<p>Men bluster. Women preen.</p>\
<p>Men break barriers. Women co-opt broken barriers.</p>\
<p>Men design. Women utilize.</p>\
<p>Men self-serve. Women self-delude.</p>\
<p>Men fuck. Women barter.</p>\
<p>Men are funny. Women are melodramatic.</p>\
<p>Men look at the sun. Women look in the mirror.</p>\
<p>Men sexualize. Women characterize.</p>\
<p>Men eat. Women indulge.</p>\
<p>Men aspire. Women inspire.</p>\
<p>Men love freely. Women love desperately.</p>\
<p>***</p>\
<p>This post is bitch bait. It&#8217;s been booby-trapped. We&#8217;ll \
see who trips it.</p>
'

c5 = epub.EpubHtml(title='why do conservatives sanctify women',
file_name='conservatives.xhtml',
lang='en')
c5.content='<h2>Why Do Conservatives Sanctify Women?</h2>\
<p>Reader LoboSolo sent me <a href="http://townhall.\
com/columnists/PaulGreenberg/2010/03/03/women_know?page\
=full&amp;comments=true" target="_blank">this article\
</a> by conservative writer Paul Greenberg extolling the\
&#8220;innate superiority\
&#8221; of women.</p>\
<blockquote><p>I&#\
8217;ve never been much of a believer in historical theories about\
the Indispensable\
Man. There may be some examples &#8212; Washington,  Lincoln,  Moses\
&#8212; but they are few. But the indispensable woman,  I believe\
in. Call it Greenberg&#8217;s Law: Women are the innately\
superior sex. My theory may not be backed by any scientific evidence,  but\
it&#8217;s something every man has surely felt. At least if\
he&#8217;s got a lick of sense. [&#8230;]</p\
>\
<p>When it comes to great truths,  each generation shouldn&#\
8217;t have to work them out by itself. They don&#8217\
;t have to be written down,  any more than the English constitution is\
. Every boy soon learns that women seem to know intuitively what the\
weaker male\
sex may grasp only by effort and education. Which is why it requires marriage\
and family to civilize the male animal. He needs a woman&#8217;\
s tutelage.</p></blockquote>\
<p>Greenberg tells a story,\
among others,  which purports to demonstrate unassailable female virtue:</p>\
<blockquote\
><p>Brighter boys learn the lesson of female superiority early; dimmer ones\
may never catch on. A story: It was homecoming weekend many years ago\
in Pine Bluff,  Ark.,  and a clump of us stood on Main Street\
waiting for the black college&#8217;s high-stepping marching band to\
come striding by,  drum major and majorettes and 76 trombones and all.</p\
>\
<p>A venturesome little boy in the group stepped off the curb\
to look way up the street &#8212; where the little girl on the\
Sunbeam Bread sign,  a local landmark,  still swings endlessly to and fro.\
Way in the distance,  the boy spotted the prancing majorettes\
throwing their batons high\
,  higher,  highest,  catching them on the beat. &#8220;Wow\
!&#8221; he exclaimed,  returning to report what he&#8217;d\
seen. His conclusion: &#8220;Girls have to know so many things\
!&#8221;</p></blockquote>\
<p>Lovely stories,  Mr.\
Greenberg. Now let me tell you a story.</p>\
<p>\
I&#8217;ve seen things you gullible chumps wouldn&#8217;t\
believe. Married women&#8217;s loins on fire off the rumpled sheets\
of my bed. A feminine Russian woman,  her buttocks turned in my direction\
,  sweetly asking me if I&#8217;d &#8220;like to\
do her in the ass&#8221; as her cell phone rings with the\
plaintive wail of her husband seeking her whereabouts. I&#8217;ve watched\
nipples harden in the dark near the cathedral gate,  and behind\
the rectory doors\
. I&#8217;ve lain with the most virtuous women you could imagine\
&#8212; caring women who &#8220;have to know so many things\
&#8221; and who give dollars to homeless bums and who tear up during\
sad scenes in the movies &#8212; who freely allowed my member to violate\
them in every conceivable way in their husband&#8217;s and boyfriend&#\
8217;s beds,  their writhing bodies,  ecstatic moans,  and gushing furrows\
testament to the lustful abandon with which they unshackled\
themselves of that other conservative virtue\
,  fidelity. I once counseled the most darling woman &#8212; a young\
woman so exquisitely gentle and winsome I&#8217;d dare any man not\
to fall instantly for her &#8212; to stop her flowing tears for our\
doomed affair and,  there on the sidewalk in midday,  to return to her\
husband at her apartment which was two blocks down the street;\
the husband who ,  through years of his toil and love,  put a roof\
over her underemployed\
head in one of the ritzier neighborhoods of the city. I have made love\
&#8212; God&#8217;s highest expression of devotion to His creation\
&#8212; with women in the company of small woodland creatures,\
scandalized roommates\
,  and children who were,  as best we dared,  out of earshot of\
our erotic rustlings. I have witnessed women,  caught in the snare\
of irrefutable\
evidence damning their supposed virtue,  lie with the effortlessness\
of a soulless sociopath.\
In the moment of release,  when we come closest to touching the Hand of\
God,  I have been instructed by a wondrously virtuous woman to &#8220;\
rape her&#8221; and to &#8220;do it like you mean\
it&#8221;. Her screams of howling joy &#8212; pain or pleasure\
I could not tell &#8212; to this day echo in my memories.\
And,  most enlightening of all,  I have seen wives and girlfriends,  their\
hearts once filled with seemingly endless and nourishing love,  cruelly\
turn on their daft\
former lovers with a vengeance unmatched by even a wronged God. Such as the\
time a sizzlingly sexy brunette whose mouth I was gracing with the\
metaphorical appendage of\
God&#8217;s divine love answered a phone call,  mid-oral\
delight,  from her ex-fiancee (who it should be noted was recovering\
from a mental breakdown) to thank him for purchasing a $5,\
000 Tempur-Pedic mattress delivered to her apartment two weeks earlier.\
Her thank\
you&#8217;s sounded surprisingly sincere for a woman whose free hand was\
simultaneously cradling the fleshy pod holding the life-giving seed\
of another man.</\
p>\
<p>All those moments will be lost in time,  Mr\
. Greenberg,  like tears in rain.</p>\
<p>What is\
it with conservatives and their willful blindness to the true\
nature of women? Pedestalization\
of the Other (and its many permutations,  c.f. &#8220\
;noble savage&#8221;,  &#8220;gaiaism&#8221;,  &#\
8220;diversity&#8221;,  and &#8220;na&#8217;\
vi&#8221;) is a sickening act of self-abasement; a\
desperate denial that one could possibly be right when one has been so badly\
wronged,  or that a wrongdoer could possibly be as bad as the facts\
attest. Perhaps those who engage in this sort of faith-based pedestalization\
of women are deathly afraid to confront the reality of female nature\
              because it\
would impose on their tidy worldview. Perhaps they need a savior,  in\
the form of women,  like of god,  to compartmentalize the darkness and\
symbolize something to aspire to. After all,  if women are just as\
bad as men,  where does that leave the sensitive man? Stuck now\
with double the responsibility to guard oneself against predation by\
              both sexes,  and\
to discard to the ash heap cherished notions of the fairer sex. Does\
this sound familiar? If you thought &#8220;beta&#8221;,\
you&#8217;d be right.</p>\
<p>Where\
conservatives sanctify women,  liberals demonize men. Not all\
              conservatives and not all\
liberals,  but enough of them that a valid generalization can be made.\
Whether sanctifying women or demonizing men,  the end result is the same:\
laws,  policies,  and cultural beliefs that are anti-male,  and\
which we in the West are soaking in today.</p>\
<p\
>I believe the conservative&#8217;s and liberal&#8217;\
s instincts toward women can be explained by contrasting the\
              peculiar life conditions of\
both:</p>\
<ul>\
<li>Conservatives,  having grown\
up in larger,  more intact families than liberals,  and being thus surrounded\
by more sisters,  aunts,  and female cousins on a daily basis,\
are loathe to imagine those female relatives could be the alpha cock-hungry\
animals inside that they really are. Liberals,  meanwhile,\
              hailing from broken\
homes and guided under the tutelage of man-hating single moms with a\
revolving bedroom door,  find it easier to grasp the amoral nature of women\
.</li>\
<li>Conservatives have less sexual experience with women than\
do liberals. I would not be surprised if it was discovered that liberal\
men lost their virginity at an earlier age than conservative men.\
              Nothing teaches\
like experience.</li>\
<li>Conservatives believe women are morally child\
-like compared to men,  that women are the weaker sex,  and\
so cannot be held accountable for their actions. Liberals,  who see white\
male oppression behind every human group difference,  are more\
              likely to individualize a\
woman&#8217;s bad actions and politicize a man&#8217;\
s bad actions.</li>\
<li>Conservatives are ashamed of their\
base desires. Thus,  they recoil at the thought that the women they\
desire might share the same debased thoughts that they do. Liberals,  by\
contrast,  are proud of their base desires. And so they are more\
accepting of the knowledge that women are as depraved as men.</li>\
<\
li>Religious conservatives fear sex for its power to distract from god. It\
is better for them that women are thought of as empty vessels incapable\
of making\
sex-based calculations in their decisions. Secular liberals love sex for\
its power\
to distract from considering the merits of any moral code. It is better for\
them that women are thought of as sex-possessed tankgrrls ready to\
rumble across\
the Vaginot Line of mind-body liberation.</li>\
<li>Conservatives\
invest more in the idea of family than do liberals. A wanton woman is\
a grave threat to that idea,  graver than even a wanton man,  for\
reasons clearly elucidated by evolutionary biology. Ergo,  women\
cannot possibly be as wanton\
as men.</li>\
<li>Conservative women are busier being pregnant and\
/or fatter than liberal women,  and are thus less frequently able to act\
wantonly. This may skew conservative men&#8217;s impressions of women to\
being something more positive than it really is.</li>\
<li>Conservatives\
by temperament are drawn to the beautiful. Liberals by temperament are\
drawn to the\
degraded. Conservatives have trouble tainting with dark knowledge the\
beauty of a woman in\
her prime. Liberals relish the thought that a beautiful young woman\
kwould wallow in\
the mud just as enthusiastically as they do.</li>\
</ul>\
<\
p>As a man who is drawn to both the beautiful and the degraded\
,  my aim is to act as a bridge between conservative men and liberal men\
,  holding the liberal&#8217;s hand tenderly to the conservative&#8217\
;s crotch. I shall bring understanding between the two mortal enemies,  and\
together we shall march into the nearest bar,  our minds fortified\
with the knowledge\
of women&#8217;s true natures and our hearts swollen with masculine conceit\
,  and lay waste to that place,  claiming battalions of pussy for our own\
. Without excuse,  without apology. Without god,  whether\
supernatural or political.</\
p>\
<p>Women are vile creatures at heart,  just as men\
are. An ugly truth,  Mr. Greenberg,  which even God can&#\
8217;t shield you from. Don&#8217;t let the batting eyelashes fool you.</p>\
'


c6 = epub.EpubHtml(title='heady pettiness',
file_name='heady_pettiness.xhtml',
lang='en')
c6.content='<h2>Heady Pettiness</h2>\
<p>I was with a girl shopping for assorted consumerist baubles. Technically\
,  she was shopping and I was providing color commentary. A man must learn\
to amuse himself to pull through these dreaded moments. In the middle of a\
well-delivered quip,  I noticed from the most distant corner of my eye\
a familiar jeans-covered ass. I studied the ass for a bit and\
the flow of hair down the back and realized it was one of my exes\
. She turned around and confirmed for me it was her.</p>\
<\
p>She didn&#8217;t see me. I watched her for\
a bit. The three years were not kind to her. Her body was\
still great but her face looked drawn,  eyes sad,  and was that an\
incipient turkey gullet? When I dated her she was a solid 8,  and\
sexy as hell. Now? A 7. Barely. In just three years\
she dropped a full point. I wondered if she had gone through an emotionally\
draining divorce in the time since I&#8217;d known her. She\
was at the store alone on a day in which most women are shopping with\
their partners.</p>\
<p>My time spent with her had been\
good. I held no ill will toward her. We departed not as exes\
,  but as former lovers,  blessedly free of bitterness or rancor. And yet\
,  when I saw my ex there in the store,  and mentally noted that\
the girl I was with was better looking than her,  a sadistic urge to\
flaunt my latest lover and parade her past my ex like a trophy float overcame\
me. I maneuvered myself and my female company into visual range of my ex\
. I refrained from looking over. I wanted the <a href="https\
://heartiste.wordpress.com/2007/10/15/bumping-\
into-exes/" target="_blank">bump in to feel natural</a\
>. (Had my lover been less attractive than my ex,  I would&#\
    8217;ve hid behind the clothes racks and rushed us out of the\
    store.)</p>\
<p>As I maneuvered closer to my ex\
through the aisles of clothes and kitchenware,  I placed my hands lovingly on\
various erogenous zones of my companion&#8217;s body. All while\
pretending not to notice my ex. I slid my hand down my lover\
&#8217;s back,  played with her hair,  and made sure\
to tell a joke so that she giggled girlishly within earshot of my ex\
. Unfortunately,  my ex didn&#8217;t notice. Either she\
was captivated by the 40% sale on hand towels,  or she was\
expertly avoiding acknowledging my presence. I doubted the latter,  \
because usually even\
the best actresses cannot hold it together with zen-like calm and serenity\
when bumping into an ex who left such an indelible impression on them.\
They give away their true feelings with a nearly imperceptible \
quiver in the shoulders\
,  or a nervous dart of the eyes.</p>\
<p>\
Had she forgotten me? Not possible. We dated too many months,\
and I&#8230; did things&#8230; with her that assured\
a memorial to me would forever be etched in her brain,  like a\
Vietnam Lovers Memorial of sex acts. Or maybe she didn&#8217;\
t recognize me? I *was* wearing a hat,  crisply turned\
down along the front brim.</p>\
<p>Nevertheless,  no\
matter how much I maneuvered,  I couldn&#8217;t needle my\
ex with my profound pettiness. She remained steadfastly\
unaware of my presence,\
flitting about the store like a hummingbird. What a wasted opportunity for a\
deliciously ego-massaging bump in.</p>\
<p>I told\
my girl about my ex being alone in the store,  and how I\
was trying to get the ex to see us. I also told her\
she was hotter than my ex. Instead of chastising me for my immaturity\
,  her eyes lit up with conspiratorial glee and she offered a strategy.</\
p>\
<p>&#8220;Ooh,  I&#8217;m\
curious. Which one is she? Let&#8217;s walk by\
her and I&#8217;ll stick my ass out for you to\
smack. Yay!&#8221;</p>\
<p>God bless women\
. Just when you are about to resign yourself to the thought that they\
are made of nothing but sugar and spice and everything nice,  you are\
reminded of the arsenic laced within.</p>\
<p>We left\
the store mission unaccomplished. I pondered for a second why I relished the\
thought of rubbing my happiness in the face of a sad,  possibly single\
ex for whom I had nothing but warm feelings. I had released the\
id monster from its hindbrain depths,  and danced a little jig with it\
.</p>\
<p>I guess it just feels too good.\
And I&#8217;ve no doubt she would&#8217;ve\
done the same had the shoe been on the other foot. Any woman\
would&#8217;ve done the same. But don&#8217;\
t bother asking them. They&#8217;ll deny deny deny.\
They&#8217;ve got an image to burnish,  you see.</\
p>\
<p><em>Note: As with many of my\
posts,  the chronology of this post has been altered to protect the innocent\
. Namely,  me.</em></p>
'

c7 = epub.EpubHtml(title='female dictionary',
file_name='female_dictionary.xhtml',
lang='en')
c7.content='\
<h2>Better Than Again: The Female Secret Code Decoder Dictionary</h2>\
<p>A wealth of experience with women will clue a man into the\
dissonance between a woman&#8217;s words and actions,  and gradually lead\
him to discover that the woman&#8217;s word is the exact inverse\
of what she wishes you to presuppose it is: not a verbal descriptive but\
rather a psychological misdirection to lull the unsuspecting,  including \
herself,  to cogitate on\
the opposite of what is,  in fact,  <a href="https://\
heartiste.wordpress.com/2008/09/09/better-than\
/" target="_blank">true</a>. Resist the temptation to blame a\
woman for her subterfuge because,  in another example of \
empirics catching up to folk\
wisdom,  <a href="http://www.nytimes.com/2009\
/01/25/magazine/25desire-t.html?_r=\
1&amp;pagewanted=all" target="_blank">science is revealing\
</a> that not even she is aware what currents ripple through her vagina\
.</p>\
<p>On that prologue,  here follows a handy dandy\
secret girl code decoder crib sheet. Though you have been weaned \
since toddlerhood,\
when your flaccid tot dong jutted out at a continual 90 degree angle to your\
raisins,  to believe the last in each series is to be aspired to,\
the truth is that,  if sexnlurv with the sexynlurvly hot babes is what you\
want,  then you are far better off being deemed the opposite by the fairer\
sex.</p>\
<p>douchey &gt;&gt;&gt;\
nice guy</p>\
<p>asshole &gt;&gt;&gt\
; sweet</p>\
<p>jerk &gt;&gt;&gt\
; cute</p>\
<p>bastard &gt;&gt;&gt\
; good man</p>\
<p>pig &gt;&gt;&\
gt; gentleman</p>\
<p>insane &gt;&gt;&\
gt; dependable</p>\
<p>jerk &gt; sexy &\
gt; hot &gt; cute &gt; sweet &gt; creep\
&gt; nice guy</p>\
<p>creeper &gt;\
creep &gt; stalker &gt; loser &gt; nice guy</\
p>\
<p>serial killer &gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;\
nice guy</p>\
<p>mass murderer &gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt; nice guy</p>\
<\
p>psychopathic hedge fund white collar criminal &gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;\
(*phew*) &gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt\
;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt; nice guy</p>\
\
<p>nice guy &gt; pedophile (finally!)</p>\
<\
p>he makes me cry &gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt; he&#8217;s\
always there for me</p>\
<p>it&#8217;s\
so hard with him &gt;&gt;&gt;&gt;&gt;&\
gt;&gt;&gt;&gt;&gt;&gt;&gt; yeah\
,  he&#8217;s a great guy</p>\
<p>\
freak &gt;&gt;&gt; attentive lover</p>\
<p\
>cheating bastard &gt;&gt;&gt; he treats me like a\
princess</p>\
<p>you don&#8217;t see what\
i see in him &gt;&gt;&gt; he&#8217;\
s the perfect man</p>\
<p>wiseass &gt;&gt\
;&gt; funny &gt;&gt;&gt; clown &gt;&\
gt;&gt; goofy &gt;&gt;&gt; quirky &gt\
;&gt;&gt; weird</p>\
<p>mysterious &gt\
;&gt;&gt; a good friend</p>\
<p>exciting\
&gt;&gt;&gt; easy to get along with</p>\
\
<p>i don&#8217;t know how much more i can\
take with him &gt;&gt;&gt; someday we&#8217;\
ll get married</p>\
<p>he always forgets our anniversaries &\
gt;&gt;&gt; he understands my needs</p>\
<p\
>pervert &gt;&gt;&gt; sensitive lover</p>\
<\
p>he screwed my best friend &gt;&gt;&gt; i\
screwed his best friend</p>\
<p>he gets me &gt\
;&gt;&gt; i get him</p>\
<p>fucking\
asshole arrogant son of a bitch motherfucking cocksucking pike of\
steaming shit filthy fucking bastard\
mama&#8217;s boy &gt;&gt;&gt; nice guy\
</p>\
<p>selfish lover &gt;&gt;&gt;\
eats me out</p>\
<p>who are you texting? &\
gt;&gt;&gt; i promise i&#8217;m not texting\
any other guys</p>\
<p>god that was such a turn\
-on &gt;&gt;&gt; i love you</p>\
\
<p>cocky bastard &gt;&gt;&gt; sweet guy</\
p>\
<p>i never know what he&#8217;s up\
to &gt;&gt;&gt; we go everywhere together</p>\
\
<p>lover &gt;&gt;&gt; husband</p>\
\
<p>is that a girl&#8217;s voice i hear in\
the background? &gt;&gt;&gt; thanks for letting me know\
what time you&#8217;ll be home</p>\
<p>\
you&#8217;re going to shit in front of me?! &gt\
;&gt;&gt; i&#8217;ll be out in a minute,  honey</p>\
'


c8 = epub.EpubHtml(title='womanese translator',
file_name='womanese_translator.xhtml',
lang='en')
c8.content='\
<h2>Womanese-to-English Translator</h2\
>\
<p>Online translator services are really helpful in a pinch when you\
&#8217;re overseas,  but what do you do when you&#8217\
;re talking with a woman who speaks your language? American women \
speak English\
,  at least syntactically and grammatically,  but the meanings of their \
words and sentences \
often mislead as much as inform. After all,  if women said what they \
meant and spoke clearly and honestly,  wining and dining them \
with all-expenses \
paid dates would be a thing of the past. You&#8217;d \
know within a few minutes whether she was going to put out for you or \
not. And if she was interested in sex,  you&#8217;d \
know exactly how to proceed to ensure it happened.</p>\
<p>\
So for those times when you actually care what a woman says to you &#\
8212; i.e.,  those times you&#8217;re talking with \
an attractive young babe you want to crotch smash &#8212; your life (\
and sanity) would be immeasurably improved if you had a Womanese-to-\
English translator at your instant disposal. Imagine \
the following conversation:</p>\
<\
p>YOU: Hi,  can I buy you a drink?</p>\
\
<p>HER: Sure!</p>\
<p>YOU: Cool\
.</p>\
<p>HER: Thanks. [drinks up,  eyes \
                 room,  alpha male pops up out of nowhere and \
                 she leaves with him\
                 ,  laughing all the way]</p>\
<p>YOU: fuck\
.</p>\
<p>Now this is how the above conversation would go \
if you had a Chateau Heartiste Womanese-to-English Translator on hand:</\
p>\
<p>YOU: Hi,  can I buy you a drink\
? [turns on W/E Translator,  patent pending]</p>\
<\
p>HER: Sure,  I won&#8217;t turn down a \
freebie,  but it will hurt your chances to have sex with me.</p\
>\
<p>YOU: Nah,  I changed my mind. I won\
&#8217;t buy you a drink.</p>\
<p>HER\
: So&#8230; you seem kind of interesting. New around here?</\
p>\
<p>See how your life would be so much better with \
the W/E Translator at your side? Here&#8217;s another \
sample conversation that many of you will encounter in the course of \
your pickup career\
:</p>\
<p>YOU: I collect walking sticks. Come,  \
let&#8217;s go to my place. I&#8217;ll \
show you my collection.</p>\
<p>HER: Ok,  but \
nothing&#8217;s going to happen tonight.</p>\
<p>\
YOU: [dejected face] oh,  ok. Well,  can I get \
your number?</p>\
<p>HER: [gives fake number]</\
p>\
<p>Feel like a lah-hooo-ser? You \
should. But you don&#8217;t need to ever feel that way \
again with the W/E Translator (patent pending,  internationally \
                               copyrighted)! How \
would the above conversation have turned out when run through the W/ET for \
accuracy?</p>\
<p>YOU: I collect walking sticks. Come\
,  let&#8217;s go to my place. I&#8217;\
ll show you my collection. [turns on W/ET]</p>\
\
<p>HER: Ok,  but nothing&#8217;s going to \
happen tonight if you give up trying.</p>\
<p>YOU: \
    [smug face] Don&#8217;t worry,  I won&#\
    8217;t.</p>\
<p>HER: [takes your \
         arm]</p>\
<p>Beautiful love,  with an assist from\
the W/E Translator. Can a price be put on such a product\
? It can&#8217;t,  but now you can have it for\
the low low price of $49.99,  an infinity dollars-minus\
-$49.99 savings! You&#8217;d be crazy to pass\
up this opportunity.</p>\
<p>More game-changing,  dick\
-wetting,  money-saving,  sanity-sparing magic,  courtesy of the\
W/ET:</p>\
<p><span style="text-decoration\
:underline;">Before W/E Translator</span></p>\
<p\
>YOU: [making bedroom move on your wife]</p>\
<p\
>HER: [turns over] I have a headache tonight. Maybe another\
time.</p>\
<p><span style="text-decoration:underline\
;">After W/E Translator</span></p>\
<p>YOU\
: [making bedroom move on your wife]</p>\
<p>HER\
: [turns over] Can&#8217;t do it. My vagina\
is still sore from fucking my boss.</p>\
<p><span style\
="text-decoration:underline;">Before W/E Translator</span></\
p>\
<p>HER: When are you going to dust the cat\
hair balls like I asked?</p>\
<p>YOU: Sorry,\
honey,  I forgot. I&#8217;ll get right to it.</\
p>\
<p>HER: Nevermind,  I already did it. You\
obviously don&#8217;t care.</p>\
<p>YOU:\
    What?! Of course I care about you! Where did this come from\
    ?</p>\
<p>HER: Just forget about it. I\
&#8217;ll be at the spa.</p>\
<p><span\
style="text-decoration:underline;">After W/E Translator</span\
></p>\
<p>HER: When are you going to stick up\
for yourself and say no to me?</p>\
<p>YOU:\
    So this is what you mean. I get it now.</p>\
\
<p>HER: My complaint about the cat hair balls is really a\
passive-aggressive taunt directed at your repulsive feeble betatude.</p>\
<p\
>YOU: It&#8217;s refreshing to know how you really feel\
instead of making me read between the lines.</p>\
<p>HER\
: I&#8217;ll be filing for divorce in less than a year\
.</p>\
<p>***</p>\
<p>Since I doubt your\
woman will stop talking anytime soon,  the W/E Translator is useful in\
every situation. Just read these typical obfuscating female words and\
watch them transform right\
before your eyes into distilled truth.</p>\
<p>HER: I\
don&#8217;t deserve you.</p>\
<p>W/\
ET: Treat me like shit if you want to get in my pants.</\
p>\
<p>HER: I&#8217;d rather not corrupt\
an innocent man.</p>\
<p>W/ET: Your inexperience\
with women is a turn-off.</p>\
<p>HER:\
    I&#8217;m not nearly as nice of a person as you\
    are.</p>\
<p>W/ET: I&#8217\
;m really nice to jerks,  but I won&#8217;t be\
nice to you.</p>\
<p>HER: I&#8217;\
m a bit too immature to appreciate a guy like you.</p>\
<\
p>W/ET: Call me in ten years after I&#8217\
;ve ridden the cock carousel and my looks have taken a hit.</p\
>\
<p>Act now,  and we&#8217;ll throw in\
the bonus W/E Nonverbal Translator! Just hold it up to visually record\
your girlfriend or wife,  and receive a verbal confirmation of her\
real state of\
mind.</p>\
<p>HER: [scarfs down ice cream]</\
p>\
<p>YOU: [activates W/ENT]</p>\
\
<p>W/ENT: &#8220;This ice cream is more\
exciting to me than your dick.&#8221;</p>\
<p>***</p\
>\
<p>HER: [parks her fat ass on a sofa to\
         watch The View]</p>\
<p>YOU: [point W\
         /ENT at her]</p>\
<p>W/ENT:\
    &#8220;I no longer feel motivated to please you because you are\
    an uninspiring beta herb.&#8221;</p>\
<p>Amazing stuff\
! And guess what? The W/ET even has a super secret algorithm\
that can tell which words women speak are truthful. That&#8217;s\
right,  it knows what needs translating,  and what doesn&#8217;t\
! When a woman says something unexpectedly candid,  the W/ET flashes a\
green light. That&#8217;s green light for &#8220;go\
to your nearest chapel and profess your belief in a higher being,  ESP,\
and Bigfoot&#8221;.</p>\
<p>HER: You&#8217\
;re too safe and predictable for me.</p>\
<p>W\
/ET: *green light*</p>\
<p>HER: You\
&#8217;re giving me too much power and I resent it.</p\
>\
<p>W/ET: *green light*</p>\
<\
p>HER: I wish you&#8217;d stop doing as I\
say because you logically figure it&#8217;s how to avoid a crushing\
break-up.</p>\
<p>W/ET: *green\
light*</p>\
<p>There&#8217;s even a setting\
that allows you to program the W/ET so that the closer a woman\
comes to speaking the unadulterated truth,  the brighter the green\
light shines in your\
face.</p>\
<p>HER: My vagina burns for violent sexual\
adventures with an emotionally opaque,  aloof badboy who makes me\
a little scared for\
my life.</p>\
<p>W/ET: *GREEN LIGHT\
GREEN LIGHT GREEN LIGHT*</p>\
<p>Sold yet? You should\
be! $49.99 will give you such a massive competitive advantage over\
every other man it&#8217;s a wonder this product isn&#8217\
;t ILLEGAL! Buy now before the divorce lawyers find a way to classify\
the W/E Translator as Schedule I contraband! (Operators and coping therapists\
                                              standing by.)</p>
'


c9 = epub.EpubHtml(title='top qualities',
file_name='top_qualities.xhtml',
lang='en')
c9.content='\
<h2>The Top Three Qualities That Make A Girl Good Girlfriend Material</h2>\
<p>There are many &#8220;tells&#8221; women have\
that,  unbeknownst to them,  signal to the men they are dating \
their worthiness\
as long-term investments. The tell number could very well be in the\
thousands,  and,  yes ladies,  we men are attuned to all of them\
,  in greater or lesser perspicacity,  and with conscious awareness \
or,  more often\
and more insidiously,  with subconscious awareness.</p>\
<p>But there\
&#8217;s value in narrowing the list to the top three tells,\
and clarifying them for the less experienced men (betas) so that they are\
armed with the foreknowledge to actively avoid those women who would \
make bad girlfriends or\
wives. An ounce of prevention is worth a pound of cuckoldry.</p>\
\
<p>So here they are: The top three girlfriend material qualities,\
in no particular order.</p>\
<p><strong>1. She\
exercised and ate healthily before she met you,  and she continues to do so\
after you start dating her seriously.</strong></p>\
<p>Marriage\
counselors and platitudinal couples therapists can stow their poppycock\
psychology aka feminist fantasy books.\
The biggest warning sign that a relationship is about to fail is the growing\
size of the woman. The fatter and more shapeless she gets,  the more her\
man&#8217;s eyes will wander,  his empathy will wither,  and\
his heart will shut down. A girl who has spent years cultivating\
good lifestyle\
habits that ensure she retains her slender,  hourglass figure for as\
long as possible\
is a girl who,  on a fundamental emotional level,  respects men&#8217\
;s needs and seeks to fulfill them. Feminists and assorted broken cunts don\
&#8217;t care about their appearance because they loathe male desire. That\
is why they are so unpleasant to be around for longer than it takes to\
deliver a hate-fueled hot jizz payload.</p>\
<p>A\
woman who works to stay as good-looking as she can within the constraints\
of her genetic endowment is signaling that she has a generous heart\
and a magnanimous\
soul. The care with which she comports herself will spill over into care for\
your well-being and support for your aspirations.</p>\
<p><\
strong>2. She rarely disparages her girl friends or snipes about their flaws\
behind their backs.</strong></p>\
<p>The girl who is\
forgiving of her friends&#8217; flaws,  who does not feel a compulsion\
to privately tear them down in order to lift herself up,  is a rare\
jewel indeed,  for the natural proclivity of The Woman™ is to backbite,\
snark and gossip about female competitors,  real and imagined,  until\
her ego tank\
is filled to brimming again. What care should men have about this\
peculiar trait\
of the unfairer sex? I&#8217;ll tell you. If she\
&#8217;s quick and all too enthusiastic to trash her friends in private\
,  she&#8217;ll be quick and all too enthusiastic to demean your\
manhood in the privacy of her mind. And once she&#8217;s\
gone down that road,  the mental demeaning begins its twisted\
manifestation into nagging and\
sex withdrawal. Unlike a man with a vendetta,  a judgmental bitch has a\
scattershot target designator; don&#8217;t be surprised if one day her\
gun of ingratitude is aimed directly at you.</p>\
<p>However\
,  expecting a girl to be nonjudgmental at all times is \
unrealistic. Women are\
born with the neural roadmap to gossip because it aids their sex in\
maximizing resources\
for their (eventual) families. But we can draw lines between women who\
occasionally indulge this instinct and women who wallow in it like a \
pig in mud\
. When you&#8217;re with your date,  is she constantly running\
down her supposed BFFs? Does her face light up when an opportunity \
presents to\
sneer about a friend&#8217;s recent nose job? Beware,  because\
you are staring at the dark heart of <a href="https://heartiste\
.wordpress.com/2012/02/01/the-evisceration-\
of-penelope-trunk/" target="_blank">borderline personality disorder</a\
> and unfettered narcissism,  the latter a characteristic that is\
particularly galling and self\
-immolating in women when taken to unhealthy extremes.</p>\
<p>\
A girl who is patient with and tolerant of her friends will extend the same\
to you. This then is an excellent foundation upon which to build a\
relationship\
that will have to,  necessarily due to the nature of two parties\
with competing\
reproductive goals,  navigate shoals in the future. A girl like this\
will also\
be more tolerant of your manly desire,  and,  instead of cutting down her\
competition,  will work on herself so that she can compete with the best of\
them for your love.</p>\
<p><strong>3. She\
has not had many past lovers,  and she is not a constitutional flirt who\
will invite the temptation of more lovers.</strong></p>\
<p>\
Lovefacts to make a feminist&#8217;s vagina explode angrily in a shower\
of dustballs: The more partners a woman has had,  the <a href\
="https://heartiste.wordpress.com/2010/09/16/\
why-sluts-make-bad-wives/" target="_blank">more\
likely she is to divorce you</a>. Sluts really are bad long-\
term prospects for men. They are great lays,  but they are bad ideas\
as girlfriends or wives. So be on the lookout today for <a href\
="https://heartiste.wordpress.com/2008/12/29/\
its-easy-to-identify-a-slut/" target="_blank\
">any and all slut tells</a> a girl will reveal in the\
course of dating her. It could save you a divorce theft tomorrow.</p\
>\
<p>But it&#8217;s not always easy to unearth\
a woman&#8217;s sordid past (rule of thumb: your working\
assumption should be that her past is more sordid than it is modest). So\
you have to rely on other,  more immediate cues of future\
unfaithful whorishness.\
That&#8217;s where a keen eye for her propensity to switch on\
a dime into flirt mode will serve you well. Constitutional flirts,  aka <\
a href="https://heartiste.wordpress.com/2010/07/\
15/shes-a-superflirt/" target="_blank">eternal ingenues</\
a>,  while fun in the beginning for their sexual promise and alluring \
coyness,\
can quickly become stressful headaches within the confines of a\
relationship. Watch for how\
effortlessly she can segue from poised girl into seductive flirt when\
other men are around\
. Does it come a little *too* naturally for her? Then you\
,  my friend,  are playing with vagina fire. A girl who loves to\
flirt,  and indulges frequently with or without you,  is a girl who is\
one private moment in the after hours office meeting room from cheating\
on you.</\
p>\
<p>Now,  personally,  I love flirty women. So\
walking the fine line between enjoying the company of flirts and suffering\
the crassness of\
flakes has presented challenges. Obviously,  I look for women who\
moderate their urges\
to flirt. A girl who generously throws off a flirty vibe that once in\
a blue moon time because she feels especially good about the way she looks,\
or because it&#8217;s her birthday,  is no trouble to dating\
stability. The girl who flirts with her girlfriend&#8217;s boyfriend on\
a random Wednesday night because,  oh,  she wants ALL the men&#8217\
;s attention,  and burgers are half price,  is a girl you should\
consider fucking and chucking after a few months pretending you&#8217;re into\
her that way.</p>\
<p>More importantly,  does she direct\
her flirting to me,  or to the world? Some girls just can&#\
8217;t get their attention whore fix without a large audience of men.\
Other girls,  the better ones,  are satisfied getting their ego fixes \
from their\
lovers alone. If a girl I am dating likes to flirt,  but she\
finds her outlet role playing Seductress Joan with me rather than\
sidling up like the\
town courtesan to every meathead with a hungry glare,  I bump her to the\
top of my LTR potential list.</p>\
<p>I hope this\
post is equally informative for the women reading as it is for the men.\
You ladies have a duty too,  if you want to capture the heart of\
a high value man,  and keep it:</p>\
<p><strong\
>Be fit.</strong></p>\
<p><strong>Be forgiving\
.</strong></p>\
<p><strong>Don&#8217;t\
be a foul slut.</strong></p>\
<p>If you think\
about it,  that&#8217;s not asking much compared to the grind\
that the average man has to endure to claim a single pussy as his own\
.</p>\
'


c10 = epub.EpubHtml(title='quality girl',
file_name='quality_girl.xhtml',
lang='en')
c10.content='\
<h2>Quality Girl</h2>\
<p>I&#8217;m often asked &#8220;What do\
you consider a quality girl?&#8221; This is a good question,  if\
by quality we mean a girl I&#8217;d be willing to date\
long term (&gt;3 months),  to invest more than the minimal amount\
of my time and energy,  and to feel secure,  if I were so\
inclined,  in committing myself exclusively without worry that she \
might spread her legs for\
any random guy who happens to catch her alone on an especially \
drunken night and\
says the right things about how good her forehead looks in the \
reflection of the\
beer bottle.</p>\
<p>Very few&#8230; and I\
mean VERY few&#8230; women in DC have met my exacting standards of\
quality. I&#8217;d estimate that of all the girls I&#\
8217;ve dated in this city less than 10% were worthy of my\
full attention. I&#8217;d hazard to guess that if all men\
held themselves to the same high standards I do and didn&#8217;t\
kowtow to the first chick who deigned to bless them with a crumb of affection\
there&#8217;d be universal agreement among DC men that my 10%\
figure is accurate. Maybe in flyover country the number of quality \
girls hits 25\
%. In Poland it is 80%. The times have changed and quality girls are\
no longer the norm.</p>\
<p>So what makes a quality\
girl? Well,  I know what *doesn&#8217;t* make\
a quality girl.</p>\
<ul>\
<li>She has cheated\
more than three times in her life,  or has cheated more than once on\
the same boyfriend.</li>\
<li>She forgets to say &#8220\
;thank you&#8221; when you buy her a drink. Buying her\
a second drink confirms her ingratitude.</li>\
<li>She dates around\
. Dating around &#8212; specifically,  seeing more than one person \
concurrently &#\
8212; is a prerogative of men only,  for reasons having to do with\
the greater leverage <a href="https://heartiste.wordpress.com/\
2007/11/14/dont-stop-thinking-about-the\
-next-girl/" target="_self">men need to arm themselves with\
</a> to compete in a dating market that is fundamentally tilted in favor\
of women. Any girl who makes a habit of dating more than one guy\
at a time,  especially if the parallel dating lasts longer than one month,\
in order to milk her options is a bad seed. In all my years\
of banging,  one soulsaving thing I&#8217;ve learned is to walk\
away from any girl who I&#8217;ve discovered is also dating other\
men. Even if I beat the competition and win her over,  it never\
ends well.</li>\
<li>She tells you she has a <\
a href="https://heartiste.wordpress.com/2008/07/\
01/boyfriend-destroyer/" target="_self">long distance boyfriend she loves\
</a>,  then proceeds to bang you anyway. A few months later,\
you see her groping a new guy,  and she&#8217;s still\
with her boyfriend. (That relationship is doomed.)</li>\
<li>\
Her default mode is sarcasm,  negativity,  coarseness,  \
and shamelessness.</li>\
\
<li>She spends twice as much time getting ready for a house party\
than she spends getting ready for a date with you.</li>\
<li\
>She can&#8217;t control her impulse to flirt with other men\
. Double minus points if she does this in your presence.</li>\
<\
li>She doesn&#8217;t seem nervous undressing in front of you\
the first time.</li>\
<li>She fucks you on a pretense\
of less than the sum total of an hour of conversation,  and calls you\
the next day worried that your condomless sex might have \
given her something. (\
    She&#8217;s been down this road before.)</li>\
<\
li>She is proud to be on the pill and considers her dependence\
on it a carte blanche slut sanctioner instead of a safety net \
affection fortifier\
.</li>\
<li>She is cavalier about casual sex.</li\
>\
</ul>\
<p>A quality girl does the opposite of\
all the above. She doesn&#8217;t cheat,  and if\
she does she has a plausible rationale. But she will still feel bad\
about it. She is generous when it is risky to be so.\
She is positive and lifts people up,  not pushes them down to lift\
herself up. She laughs at the absurdity and beauty of the world,\
but never at the expense of others. She is warm,  and this\
is something that can&#8217;t be taught. She says &#\
8220;I love you&#8221; early and often out of conviction\
,  not inquisition. She understands that her heart is more important than her\
pride.</p>\
<p>A high quality girl is good for\
standing by,  sticking with,  supporting always,  loving fully,\
    defending righteously\
,  and if the timing is right,  embracing for life to the exclusion\
    of all others. She is the type of girl who can enthrall you\
    with her words alone. She can make you smile over the phone.\
She can be far away but feel near. She is often discovered in\
the unlikeliest places,  and her magic is the energy that animates her pretty\
    face,  rather than the other way around.</p>\
<p>\
    Low quality girls are good for fucking,  a few laughs,  some funny\
    digicam pics,  and that&#8217;s it. Spare your hard\
    -earned manly capital &#8212; your time,  your resources,  your\
    protection,  your commitment,  your LOVE &#8212; for those few quality\
    girls you might meet if you&#8217;re lucky. And speaking\
    as a man who has seen,  heard and experienced enough to turn the\
    most naive optimist into a stone cold cynic,  if you do meet a girl like\
    that,  you would be a fool to pass her up. Her kind is going extinct.</p>\
'

c11 = epub.EpubHtml(title='slut id',
file_name='slut_id_xhtml',
lang='en')
c11.content='\
<h2>It''s Easy To Identify a Slut</h2>\
<p>Women seem to think that men are too thickheaded and inattentive to\
identify which of them are cockgobbling cumguzzling sluts. Or they prefer\
to believe their\
sly poses of innocence and white lies are good enough to keep men in the\
dark about their sexual histories. They would be wrong. The dirty\
little secret\
is out: Men have finely tuned straydar for slutty women because they are the\
ones more likely to cheat. Women <a href="http://www3.\
interscience.wiley.com/journal/118999174/abstract?CRETRY=1\
&amp;SRETRY=0" target="_blank">lie more about their\
sexual pasts</a> to men and to themselves,  or otherwise expend great\
effort covering it up,  because they know that men will downgrade them\
as potential\
long term mates if their sluttiness were revealed in all\
its jizz-spackled bukkaked\
glory.</p>\
<p>Here is a list of tramp tells:</\
p>\
<ul>\
<li>She broaches the subject of sex first\
.</li>\
</ul>\
<p>The more explicitly she talks about\
sex before you&#8217;ve banged her,  the likelier she has a\
storied slutty past.</p>\
<ul>\
<li>She suggests kinky\
sex acts.</li>\
</ul>\
<p>If you&#8217\
;ve been dating a short while and she eagerly implores you for public sex\
before the glow of bedroom missionary sex has worn off,  you&#8217;\
ve got a slut.</p>\
<ul>\
<li>She&#\
8217;s neurotic and disagreeable.</li>\
</ul>\
<p>\
Emotionally flighty girls are vaginally flighty girls. They are ruled\
by their vaginas.\
If she&#8217;s the gossipy,  backstabbing,  conniving sort who <\
a href="https://heartiste.wordpress.com/2008/10/\
22/sarcasm-is-unfeminine/" target="_blank">drips with sarcasm\
</a> and generally disdains everyone around her,  you can bet her black\
soul will seek sustenance on a carousel of cock.</p>\
<ul>\
\
<li>She frequently goes commando.</li>\
</ul>\
<p\
>Yeah,  as guys,  we think it&#8217;s hot when\
we slide our hands under our girlfriends&#8217; dresses during dinner in a\
fancy restaurant and discover a panty-less pussy waiting for us,  but what\
if you notice she&#8217;s sans underwear while you&#8217;\
re both shopping in Whole Foods? At a family picnic? In church?\
On a ferris wheel? In a glass elevator? You get the picture.</\
p>\
<ul>\
<li>She&#8217;s got that\
crazy,  hyper,  coked-up look in her eyes.</li>\
</\
ul>\
<p>Welcome to attention whore land! Chicks who can&#\
8217;t breathe without being the center of attention are chicks who are unable\
to control their craving for fresh cock. You want to be on the lookout\
for manic depressives and girls who can&#8217;t make it through a\
ten minute conversation without screeching in phony excitement.</p>\
<ul>\
<\
li>She shows a lot of cleavage all the time.</li>\
</\
ul>\
<p>No worries if she&#8217;s accentuating her\
tits on the first date to entice you,  but if she&#8217;\
s got those colliding death stars displayed for the world to admire\
every time you\
&#8217;re out with her,  you&#8217;ve got a\
woman on your hands who is addicted to advertising herself. And there will be\
buyers,  oh yes!</p>\
<ul>\
<li>She *\
really* seems to know what she&#8217;s doing in bed.</\
li>\
</ul>\
<p>Hey man,  nothing like getting a\
BJ from a chick who knows how to hit the underside with her tongue,\
but it does make you wonder how much dick it required for her to reach\
that level of professionalism.</p>\
<ul>\
<li>She has\
an impressive collection of vibrators and admits to wacking off to porn.</li>\
\
</ul>\
<p>She&#8217;s a high testosterone sex\
fiend who values sexual novelty more than pair bonding. This type of girl is\
a creature of her id. High T girls are easy to spot. Check\
for forearm hair,  narrow hips,  broad shoulders,  a penchant for cursing,\
a flat ass (adjusted for race),  career ambition,  and status whoring.</\
p>\
<ul>\
<li>She asks you how many women you\
&#8217;ve slept with or accuses you of being a player.</li\
>\
</ul>\
<p>One word: projection.</p>\
<\
ul>\
<li>She seems &#8220;hard&#8221;.</li\
>\
</ul>\
<p>If she&#8217;s got that\
tough,  tankgrrl aura about her,  like she&#8217;s been through\
dating hell and back,  and her cynicism is worse than yours,  you know\
she&#8217;s been used like a cheap whore.</p>\
<\
ul>\
<li>She&#8217;s incredibly circumspect or incredibly forthcoming\
about her past or sex in general.</li>\
</ul>\
<p\
>In the course of a few dates,  occasionally the conversation turns to past\
loves or sexual experiences,  or views on men and women and the dating scene\
. Normally,  these exchanges are blessedly brief and act as\
useful springboards for other\
topics,  but when she seems like she&#8217;s hiding something big\
you&#8217;ve got a right to be suspicious. Listen for tells\
that give the game away. Stuff like &#8220;Oh well,  we\
all have our skeletons&#8221;. Or &#8220;I&#8217;\
ve learned so much growing up.&#8221; Or &#8220;Men are\
pigs.&#8221; (The last one usually said by a record breaking slut\
.) Naturally,  you want to write off any girl as GF material who brags\
about her CRAZY and WILD college years. Believe me,  those years included more\
than college.</p>\
<ul>\
<li>She&#8217;\
s an artsy type.</li>\
</ul>\
<p>Or a\
lawyer. See: <a href="https://heartiste.wordpress.com\
/2008/09/17/how-to-handle-femmes-\
fatales-part-2a/" target="_blank">Eternal Ingenue</a>\
and <a href="https://heartiste.wordpress.com/2008/\
09/18/how-to-handle-femmes-fatales-part\
-3/" target="_blank">Amazonian Alpha</a>. The paradox of\
femininity is that it is often both the ultrafeminine and\
ultramasculine women who have racked\
up big numbers of men.</p>\
<ul>\
<li>She\
tells you about all the places she&#8217;s traveled.</li>\
\
</ul>\
<p>Yeah,  chicks love to travel,  but how\
many have put their dreams into action? If your date has been around the\
world twice with multiple stops in Rome,  Rio,  Vegas,  LA,  or\
some Appalachian backwater you can be sure she&#8217;s &#8220;\
traveled&#8221; straight into the crotch of an exotic local\
at every destination\
.</p>\
<ul>\
<li>She never has a break between\
men longer than one week.</li>\
</ul>\
<p>If\
she&#8217;s the type who can&#8217;t stand to\
be single and monkey swings from one man to the next,  sometimes with sperm\
-sharing overlap,  odds are high she&#8217;s a slut.</p>\
<ul>\
<li>You&#8217;re tapping her for the first time and\
she doesn&#8217;t remind you to put on a condom.</li\
>\
</ul>\
<p>We men have an excellent fallback system for\
flushing out the sluts. If we think you&#8217;ve been around\
,  we act as if we&#8217;re going to rawdog you,\
only to reach for the condom at the last possible second. If you haven\
&#8217;t reminded us to put one on during the long pre-\
penetration buildup,  and it looks like you&#8217;d have been OK\
taking our unwrapped meat,  we have all the evidence we need that you&#\
8217;re a skank.</p>\
<ul>\
<li>She\
never stops shit testing you.</li>\
</ul>\
<p>A\
girl who is constantly testing you for alpha congruency is a girl\
who would jump\
to another man the moment you betatize yourself. Worthy girls keep\
the shit testing\
to a bare minimum. Turn on your love light,  baby.</p>\
\
<ul>\
<li>She buys you a lot of gifts.</li\
>\
</ul>\
<p>I&#8217;m not sure why\
this is a leading indicator of sluttiness,  but in my experience it is.\
Especially if she showers you with little gifts early in the\
relationship. I open\
the floor to a discussion of theories for this particular observation.</p>\
<\
ul>\
<li>She&#8217;s OK with making out in\
bars.</li>\
</ul>\
<p>Self-explanatory.</p\
>\
<ul>\
<li>She lets you snort coke off her ass\
.</li>\
</ul>\
<p>Oh yeah,  big time slut\
.</p>\
<ul>\
<li>She&#8217;s black\
.</li>\
</ul>\
<p>Sorry,  folks,  hate to\
say it,  but going by my personal experience and what I&#8217;\
ve heard from friends,  black chicks seem to sleep around more. Don&#\
8217;t blame me,  I&#8217;m just the Deliverer Of\
Truths Best Left Unsaid But I&#8217;m Going To Say Anyhow.</\
p>\
<ul>\
<li>She has a lot of slutty friends\
.</li>\
</ul>\
<p>Ye shall know her by her\
support group.</p>\
<ul>\
<li>Her cunt is cavernous\
.</li>\
</ul>\
<p>Some of you wonder if this\
is an urban legend or a frat boy joke,  but it&#8217;\
s got a kernel of truth. If you feel big with most girls,\
but small with her (and she doesn&#8217;t have the excuse\
                    of being a seacow),  she has a stretched out pussy\
that has happily\
accommodated a parade of giant cocks. Why do you think Kegels are all the\
rage with the city slutterati? Chicks are onto the fact that their\
distended pussies\
betray their loose ways,  and anything to tighten up that love hole helps them\
hide their pecker pounded tracks. When I feel humongous with a girl,  I\
know she has a normal sized snatch that hasn&#8217;t been used\
like the town orifice. The more I feel like I&#8217;m\
ripping her insides to shreds,  the likelier I am to move her to the\
front of my cherished girlfriend queue.</p>\
<ul>\
<li>\
Your gut tells you she may be a slut.</li>\
</ul>\
\
<p>Always go with your gut. It will almost never lead you\
astray.</p>\
<p>****</p>\
<p>A lot of\
guys,  particularly artsy fartsy greater beta males whose agenda is to\
ingratiate themselves to\
women with a fawning act of white knighting nonjudgmentalism drivel,\
believe that it is\
wrong to categorize women by sluttiness,  let alone to disqualify\
them as relationship candidates\
based on how many hot loads to the face they took over the course of\
their sexually active lifetimes. &#8220;Don&#8217;t judge!&#\
8221; is the rallying cry of weak women and lickspittle betas and\
lesser alphas\
everywhere. Conveniently forgotten in this social stampede to shame\
male standards out of existence\
is the fact that judgement is inherent to human nature. The\
frontlines of judging\
eyes are everywhere. We all do it,  including those who judge others for\
exercising their judgement. If sluttiness were just another lifestyle\
choice with no implications,\
there would not be a stigma attached to the word,  nor a concerted effort\
to enforce compliance with the equalist world order by the guardians of\
female prerogative and\
pushers of beta male submission howling with inflamed passion at the\
injustice of men who\
dare to promote less promiscuous women at the expense of sluts for\
the best of\
their masculine love and attention.</p>\
<p><strong>Note:</\
strong> As a tactical matter,  it\
&#8217;s recommended to refrain\
from being judgemental of the sexual history of\
girls you are gaming. Naturally,\
you don&#8217;t want to\
deep six a budding romance before you\
&#8217;ve closed the deal.\
There will be plenty of time post\
-sex for you to take a measure\
of the girl&#8217;s\
sluttiness and screen her for lesser or greater\
commitment. I think this goes without\
saying,  but apparently there are some commenters\
who believe being completely nonjudgemental of anything\
a woman does is the mark of an\
alpha. In fact,  it&#\
8217;s just the opposite. Only\
alphas have the market value to mercilessly\
judge the women they choose to bring into\
their lives.</p>\
<p\
>Men subconsciously judge women&#8217;\
s sluttiness for eminently practical reasons,\
just as women judge men on a host\
of alpha benchmarks for similarly practical reasons\
. No moral equation required. &#8220\
;Slut&#8221; is,\
in fact,  a morally neutral term in\
the context of the sexual market,\
where a slutty girl is viewed,  justifiably\
,  desirably as an easy lay who\
will go all the way right away,\
and undesirably as a girlfriend or wife\
prospect in whom to invest precious resources.\
With the law and social institutions of\
the modern west arrayed against male interest as\
it hasn&#8217;t been in all of human history,  it is\
of critical importance that men get this part of choosing girls for <a href\
="https://heartiste.wordpress.com/2008/08/26/\
quality-girl/" target="_blank">long term investmest and wife and mother\
potential</a> down to a science. <a href="https://\
heartiste.wordpress.com/2008/03/11/mandatory-paternity\
-testing-has-arrived/" target="_blank">Mandatory paternity testing</\
a> will aid them in this,  and I predict such testing will seismically\
shift the playing field in a way we haven&#8217;t seen since\
the introduction of the pill and widespread use of the condom.\
While most married\
men are not soulkilled by cuckoldry,  it only takes a radical change at the\
margins to have a huge effect on the behaviors of the whole.</p>\
\
<p>For those of you new to the Wonderworks that is Poon,\
don&#8217;t bother bitching ineffectually like a wind-up Jezebel lezbot\
about &#8220;<a href="https://heartiste.wordpress.com/\
2007/04/13/double-standards/" target="_blank">double\
standards</a>&#8220;. They are a fact of deeply ingrained sex differences\
,  and aren&#8217;t going anywhere. No one said life was\
fair.</p>\
<p><strong>Maxim #41: The more\
experience you have with women,  the more you&#8217;ll know which\
women have experience with men.</strong></p>\
<p><strong>\
Corollary to #41: It is the inexperienced beta male who is most often\
in the dark about a woman&#8217;s sexual history and liable to\
be victimized by the cheating slut.</strong></p>\
<p>The\
<a href="http://www.physorg.com/news10824.html\
" target="_blank">median number of sex partners</a> for American\
women is 3(!). The average is 8.6. This means that there\
is a group of super slutty women,  let&#8217;s call them\
&#8220;girls who live in the big blue coastal cities and work in\
marketing or PR&#8221;,  who are shifting the average higher for all women\
. By these numbers,  it is fair to conclude that a woman who has\
had more than the median number of partners is a candidate for\
slut designation,\
and the higher her number the sluttier she is.</p>\
<p>\
0 lifetime partners: Sweet virginal manna. A bit weird,  but you&#\
8217;re confident you&#8217;ll break her in.<br />\
\
3 lifetime partners: Typical woman. Wife and mother of your\
children material.<\
br />\
10 lifetime partners: Above average. Proceed with caution.<br />\
\
15 lifetime partners: Well above average. Be dominant or she&#8217;\
ll cheat.<br />\
25 lifetime partners: A whole lot. Use her\
and lose her.<br />\
100 lifetime partners: Stopwatch material. You wonder\
how fast you can get her from &#8220;Hi&#8221; to\
&#8220;Spread your ass cheeks,  I&#8217;m going in\
&#8221;.</p>\
<p>I suspect that overall female sluttiness (\
    actual penis in vagina sluttiness,  not sluttiness as defined by\
    proxy fashion trends\
) has increased slightly over the past 40 years,  with the blue state city\
chicks fucking around more than ever and the red state religious girls\
fucking around less\
. It goes without saying that only the top 20% of men are enjoying\
the emergent slut bounty.</p>\
<p>What men think about sluts\
,  illustrated:</p>
'


c12 = epub.EpubHtml(title='jobs ',
file_name='jobs.xhtml',
lang='en')
c12.content='\
<h2>What a Girl''s Job Tells You</h2>\
<p>Here are my opinions of the sexual and relationship\
compatibilities of girls\
with the following jobs:</p>\
<p><strong>ADDENDUM:</strong\
><br />\
Some of the commenters mentioned I left interns and staffers off the\
list.  I count these girls as part of the hr/marketing/pr\
brigade except they are burdened with much bigger egos,\
self-righteousness,  and\
workaholic issues.  They all secretly want to hook up with an\
older powerful man\
.  They disdain artist types.<br />\
<em>SSR:  full erection\
(come on,  they&#8217;re all under 23. rigidity guaranteed\
 )<br />\
LTPR:  varies (are you a congressman? lock her\
               in. if not,  use her and lose her)</em></p\
>\
<p>It was an oversight by me to leave off saleswomen.\
See: Lawyer and HR/Marketing/PR.  Much depends on how well\
she does in sales.  Because sales is so inegalitarian in how the\
field dispenses\
its rewards,  you have to make a distinction between weekend\
warriors and the true\
success stories.  Is she a dilettante real estate agent?  She&#8217;\
ll be grounded and feminine.  Consider a long term investment in her.  Did\
she turn $250K in commissions as a pharm sales rep?  She&#8217\
;s just as alpha and ballcutting masculine as the BIGLAW lawyer.\
Just remember\
,  if she can compete with the most aggressive MEN and still come out on\
top,  her vagina is coated with radioactive juices.</p>\
<p>\
Note on lawyers:  Just because she may work for a non-profit doesn\
&#8217;t make her a kinder,  gentler woman.  In fact,\
some of the most cutthroat lawyers work at non-profits since\
those positions are\
in demand and in short supply.  Moralism and megalomania is\
never a good combination\
.</p>\
<p><strong>Lawyer</strong></p>\
<\
p>Amoral alpha males with vaginas.  Their yin is so deeply buried they\
spend all their free time (2 hours per week) fantasizing about a powerful\
dominant man releasing their inner woman.  This is your cue to ratchet up the\
assholery.  Outside of i-bankers and fashionistas,  you will not meet a\
more materialistic or status-conscious chick than a lawyer.  When she\
inevitably starts\
talking about what law school she attended and politicos she knows,\
put your finger\
up to her mouth and say <em>&#8220;shhh&#8230;\
stop.  from now on we will talk about happy things.  tell me only\
the good things that come to mind about your childhood.&#8221;</em>\
Most lawyer chicks have large clits which they use to pin you down on the\
bed.  Making love to a lawyer means facefucking her till she pukes a little\
.  The gods of karmic retribution will be pleased with this.  Lawyers\
are always\
fucking over everyone else so this is your chance to return\
the favor.  Proceed\
with great relish.<br />\
<em>Sexual Satisfaction Rating:  4/\
5th erection<br />\
Long Term Potential Rating:  don&#8217;t\
be a masochist</em></p>\
<p><strong>Human Resources\
/Marketing/Public Relations (99% of all women)</strong></p\
>\
<p>Since so many women work in these preposterous fields,  it\
is hard to say anything definitive about them as romantic partners.\
The only conclusions\
we can draw are that these women are people-persons (shocker!) and\
have ADD.  They could not sit still for a minute and reduce a fraction\
if their lives depended on it.  They are intuitive and fiercely catty,  but\
also practical.  In fact,  conventional wisdom to the contrary\
notwithstanding,  women are\
more practical than men.  Let her believe you think her job is important and\
she will spread her legs for you unbidden.<br />\
<em>Sexual\
Satisfaction Rating:  2/3rd erection<br />\
Long Term Potential Rating:\
    3/4 carat</em></p>\
<p><strong>\
Engineer (0.00001% of all women)</strong></p>\
<\
p>If there was ever an occupation created solely for the benefit of a\
man&#8217;s intellectual strengths,  engineering is it.  So right off\
the bat you know that any female engineer will be weird.  Not\
necessarily assertively\
masculine like the female lawyer,  but not typically feminine either.\
Female engineers are\
the Holy Grail of male nerddom.  Every nerdo anime fanboy\
with Dungeon Master on\
his resume dreams of meeting and falling in love with a cute nerdgirl WHO IS\
EXACTLY LIKE HIM so that his autistic social retardation doesn&#8217;t get\
pushed to the breaking point like it would with a normal girl.<br />\
\
Minus: fornication mysteriously happens in between lengthy dissertations\
on string theory.<br />\
Plus: she can assume sex positions within a millimeter of spec.<br />\
<em>Sexual Satisfaction Rating:  1/4th erection<br />\
Long\
Term Potential Rating:  5 carats</em></p>\
<p><strong\
>Elementary School Teacher</strong></p>\
<p>Pure gold.\
Put this girl on your short list for long term commitment.  What&#8217\
;s not to love about the elementary school teacher?  Cute,  thin (\
it&#8217;s a workout chasing kids all day),  ultra feminine\
,  nurturing,  selfless,  caring,  and most importantly blessedly\
    low maintenance due\
to the nature of her workplace environment sequestering her from the\
    attentions of men\
.  The best ones teach 1st through 5th grades.  Women who supervise daycare\
are too toddler-focused and will love the kids more than you.\
You will soon tire of her coo-ing at every baby you both\
pass by.  High school teachers are too stressed out from their job to\
properly service your manly needs at home.  Don&#8217;t bother\
with college professors unless you think foreplay is listening to an\
    earful of pomo\
feminist shrillness.<br />\
Bonus:  teachers don&#8217;t make\
much money so your financial status will always be higher,  guaranteeing a long\
and healthy relationship.<br />\
<em>Sexual Satisfaction Rating:  3\
/4th erection<br />\
Long Term Potential Rating:  hope diamond (\
she&#8217;s not gonna have much opportunity to cheat at work\
)</em></p>\
<p><strong>Nurse</strong></p\
>\
<p>See:  elementary school teacher.  One caveat &#8212\
; the nurse is secretly a status whore.  Patients lean on her all\
day for comfort and assistance so when she gets home she wants nothing more\
for herself than a high status alpha male to lean on.  That is\
why you will often see nurses pairing up with military officers,\
    stockbrokers,\
and executives.  The superfeminine gravitates to the supermasculine.\
    Surprisingly,  nurses and\
doctors rarely date &#8212; perhaps they look for a partner in whom\
they can escape the human suffering they deal with on the clock,  and\
not be reminded of it at home.<br />\
<em>Sexual\
Satisfaction Rating:  1/3rd erection (full erection if she wears the\
nurse outfit)<br />\
Long Term Potential Rating:  cubic zirconia (it\
&#8217;s fun to fool status whores)</em></p>\
<p><strong>Scientist</strong></p>\
<p>\
Hidden gem.  The female scientist is reserved,  taciturn,  introspective,  shy\
,  and when they put some effort into how they look,  cute &#\
8212; all wonderful traits for a woman to possess.  They ambitiously pursue\
abstract ideas,  not material goals or oneupsmanship,  so status\
                                             competition with them\
will be minimal.  They are smart in the way people like their smarties\
&#8212; inwardly directed as opposed to outwardly manipulative.  This is a\
result of their smarts being spread out over both brain hemispheres\
                                             rather than concentrated\
in just the right like most women.  The scientist&#8217;s\
natural creativity and systematizing impulse will express itself with\
                                        magnificent attention to detail in\
the bedroom.  You will never get a better&#8230; or more\
meticulous&#8230; blowjob.<br />\
Minus:  she is ultimately rational\
and will give you exactly six months to propose.  No stringing along this\
chick.<br />\
<em>Sexual Satisfaction Rating:  serviceable chubby<\
br />\
Long Term Potential Rating:  3 carats  (frumpy clothes and dorky\
competition encourage fidelity)</em></p>\
<p><strong>Stripper\
</strong></p>\
<p>Have you ever seen an unhappy\
man dating a stripper?  The novelty,  bragging rights,  and earthshattering sex\
are worth the drama.<br />\
<em>Sexual Satisfaction Rating:\
titanium rod<br />\
Long Term Potential Rating:  hide your valuables</\
em></p>\
<p><strong>Journalist</strong></p\
>\
<p>Don&#8217;t ask me why but for\
some reason these girls have absolutely no personal ethical code\
                                             whatsoever.  Which may\
be why the journalism profession is in such disarray today and trusted by no\
one.  The she-journo will fuck around remorselessly with a dashing embed\
while her fiancee waits loyally at home for her return.<br />\
<\
em>Sexual Satisfaction Rating:  3/4th erection<br />\
Long\
Term Potential Rating:  1/24 carat</em></p>\
<\
p><strong>Artist</strong></p>\
<p>Every man\
should experience at least once in his life the joy of dating an artist chick\
.  Painters,  photographers,  singers,  freelance fiction writers,\
                                             actresses&#8230;\
their exuberant lovemaking will spoil you for all other women.\
                                    Their beautiful romantic gestures\
will capture your heart.  Their craving for intimacy and their\
wellspring of empathy will\
draw you in.  And then right at the moment you fall deepest for her\
you will catch her one night frenching a half-shaven DJ at a seedy\
club.<br />\
<em>Sexual Satisfaction Rating:  titanium rod minus refractory\
period<br />\
Long Term Potential Rating:  cracker jack box ring</em\
></p>\
<p><strong>CEO</strong></p>\
<\
p>Are you fucking kidding me?<br />\
<em>Sexual Satisfaction\
Rating:  flaccid<br />\
Long Term Potential Rating:  why bother?</em\
></p>\
<p><strong>Waitress</strong></p>\
<\
p>That&#8217;s more like it.<br />\
<em\
>Sexual Satisfaction Rating:  7/8th erection<br />\
Long Term Potential\
Rating:  1/2 carat</em></p>\
<p><strong\
>Blogger</strong></p>\
<p>If she writes a confessional\
online diary,  expect her to be passive-aggressive,  petty,  moody,\
cruel,  untrustworthy,  vengeful,  and highly libidinous.  Make a sex tape as\
soon as it is feasible so you can use it as blackmail in the event\
of post-breakup threats to out your dirty laundry on her blog.<br\
/>\
<em>Sexual Satisfaction Rating:  N/A<br />\
Long\
Term Potential Rating:  N/A</em></p>\
<p>\
I hope it hasn&#8217;t escaped anyone&#8217;s notice\
that sexual satisfaction and long term potential are inversely related.</p>
'

c13 = epub.EpubHtml(title='friends',
file_name='friends.xhtml',
lang='en')
c13.content='\
<h2>Judging A Girl By The Friends She Keeps\
</h2>\
<p>When you start dating a girl,  you will\
get to meet her friends,  sometimes sooner,  sometimes later. But\
usually within\
the first couple of months you will have been introduced to\
nearly everyone she knows\
(locally),  especially if she really likes you. Pay close attention to the\
types of friends she has (if she has any),  for that will tell\
you a lot about her long term potential. Screening a girl for LTR worthiness\
based on the friendships she keeps is a powerful tool men have\
at their disposal\
,  and one you should not overlook.</p>\
<p>The following\
categories are ranked by LTR worthiness and chance of mental instability.</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with No Friends</strong></span><br />\
LTR worthiness: Short but\
passionate fling<br />\
Chance of mental instability: Sleep with one eye open\
</p>\
<p>A girl with no friends likely has some personality\
defect that prevents her from forming bonds with people. Other\
girls regard her as\
a weirdo,  and not without justification. Men think her social\
isolation means she\
will be an easy lay. They are right. This kind of girl is\
starved for human connection with a man who &#8220;gets her&#8221\
;. Hit those buttons,  and you will enjoy a three month festival of zero\
-cost fornication. After a while,  though,  her weirdness will grate,\
and she will pull stunts that make you scratch your head in confusion. Girls\
with no friends are often brooding emo types,  or <a href="https\
://heartiste.wordpress.com/2011/07/15/cutter-\
lover/" target="_blank">cutters</a>,  and they may go batshit\
crazy if you dump them. Have a restraining order ready.</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with No Close Friends,  Only Acquaintances</strong></span><br />\
LTR\
worthiness: Pump and dump<br />\
Chance of mental instability: Hope you\
like drama</p>\
<p>The classic attention whore. The girl\
with nothing but loose acquaintances who flit in and out of her\
life craves the\
attention of hundreds,  if not thousands,  of human beings. She is usually\
a hot chick with a swollen ego who initially attracts girls into her\
reality for\
friendship,  but who then drives them away with her insatiable\
appetite for social domination\
and ego stroking. She is a known blue ball queen who gets off stringing\
along beta orbiters in sexless perpetuity. She is simultaneously\
loved and loathed by her\
girlfriends,  who find her outrageous fun at parties,  but\
insufferable in more intimate\
settings. She is frequently bad-mouthed behind her back,  and she presents\
one of the few cases where girl friends will sympathize more with\
her male suitors\
and boyfriends than they will with her. She is a high infidelity risk,\
so proceed with caution. Best used as a sperm receptacle,  if you can\
get her to give it up (not an easy task unless you know how\
to expose her soft underbelly &#8212; fear of ostracization.)</p>\
\
<p><span style="text-decoration:underline;"><strong>\
The Girl with Only Family for Friends</strong></span><br />\
\
LTR worthiness: Perennial booty call<br />\
Chance of mental instability:\
Riddled with insecurities</p>\
<p>On paper,  a girl\
who only has her family for companionship may strike you as a good LTR\
prospect. You think: Ah,  she&#8217;s grounded,\
earthy,  family-oriented,  and shuns the nightlife. But you would\
be wrong. As any man who has married a &#8220;family\
-only&#8221; girl will tell you,  they are demanding,\
mule-headed,  socially awkward,  often obnoxious and full of themselves.\
Remember,  she&#8217;s had her family telling her how great\
she is her whole life,  with no unbiased opinion from outside\
                       sources checking\
her ego. She is,  in fact,  not much different than the\
girl with no friends,  except she has decided that leaning on her family\
for support and ego gratification is better than being alone.\
                       Other girls find\
her annoying at best,  and arrogantly repugnant at worst,  and that is\
why she must retreat to the comfortable confines of family for\
                       her social needs\
.</p>\
<p>The no-friends girl at least has\
the cutesy artist angle to work; the family-only girl has nothing\
to offer but an unjustified entitlement complex. She is the classic daddy&#\
8217;s slutty princess. The family girl instinctually knows this about herself\
,  and thus will nurse barely-concealed insecurities about her true worth,\
which she will take out on you,  making your life miserable. Double\
-plus negative: You&#8217;ve gotta deal with her parents\
,  brothers and sisters ALL THE TIME. Run away (after you&#\
8217;ve plundered her ass.)</p>\
<p><span style\
="text-decoration:underline;"><strong>The Girl with Only Guy\
Friends</strong></span><br />\
LTR worthiness:  Second string girlfriend\
<br />\
Chance of mental instability: High,  if you regard manipulation\
and tomboyishness as psychological disorders</p>\
<p>What do you\
get when you surround a girl with obsequious,  supplicating betas who want in\
her panties,  and remove all contact with catty girl friends who might steal\
the attention of those mewling betas? Yeah,  that&#8217;s\
right&#8230; a self-centered user. If the girl is\
cute,  you should always cast a jaundiced eye at her if her friends\
are all men. Odds are very good that most of those men&#\
8230; actually,  all of them&#8230; want to bang her\
(and she knows this). But they aren&#8217;t.\
Their job is to mingle in her glorious presence,  polishing her pedestal and\
generally turning her into a girl who expects men to roll out the red\
carpet for her. She is the classic cocktease. She loves the intimate emotional\
connection she gets from a close circle of male friends,  without having\
to give\
up her pussy to any of them or having to deal with competitor females.\
Now you may be the most alpha alpha male of all times,  and she\
may love you for it,  but once a girl has demonstrated by her friendship\
choices that she is a user,  there will come a time,  you can\
count on it,  that she will try to use you. It&#8217\
;s best to keep her in your second tier of lovers,  where her\
machinations won&#8217;t affect you with nearly as much import.</p\
>\
<p>Caveat: If she&#8217;s plain looking and\
has mostly male friends,  the upside of her having a well-developed sympathy\
for men&#8217;s peculiar challenges outweighs the downside of her having her\
ego stroked and her emotional needs met all the time by her male friends.\
All the better if most of her male friends are alphas themselves who are in\
relationships and who don&#8217;t spend inordinate time massaging her ego.\
But then why are you dating a plain-looking girl?</p>\
<\
p><span style="text-decoration:underline;"><strong>The Girl\
with Mostly Gay Guy Friends</strong></span><br />\
LTR worthiness:\
    One night stand<br />\
Chance of mental instability: She gets her own DSM edition</p>\
<p>Same as above,  except multiplied one thousand fold. A big\
unwritten story about the decline of the West is the deleterious\
impact trendy gay men\
have had on the egos of single urban Western SWPL women. If you can\
imagine it,  try to picture her as nothing more than a\
disembodied vaginal hole\
. It will help keep a healthy emotional distance. A few gay guy friends\
is perfectly fine. Ten of them,  to the exclusion of other groups of\
friends,  is a red flag.</p>\
<p><span style="\
text-decoration:underline;"><strong>The Girl with Only Girl Friends<\
strong></span><br />\
LTR potential: High,  if you like lavish\
weddings<br />\
Chance of mental instability: Not more than the average girl\
,  which is to say,  high</p>\
<p>The good\
news about the girl with only girl friends is that she is normal and feminine\
. She likes doing girly stuff,  and if you are a real man and\
not a spotted-ass nerd with a jones for a butt-kicking babe\
who solves math proofs in her downtime,  then you will appreciate\
being the boyfriend\
of this type of socially calibrated and psychologically\
balanced girl. There&#8217;\
s nothing wrong with dating a girl who,  you know,  ACTS LIKE A\
GIRL. Another plus: she doesn&#8217;t require the ministrations of\
hordes of beta male taintlickers to keep her from downward\
spiraling into depression.</p\
>\
<p>The bad news should be obvious: she has no concept\
of what men must endure in either the dating market or the social market in\
general. Thus,  her sympathy for men is nil,  and she comes across\
solipsistic and self-absorbed. But she will happily bend to the will of\
a strong man,  because she does not shun her female nature. She makes\
a great girlfriend; a wife,  though,  is an entirely different matter.\
That same group of supportive single girl friends who loved you as\
her boyfriend will\
tirelessly work to undermine your marriage should they themselves remain in\
the purgatory of singledom\
.</p>\
<p><span style="text-decoration:underline;"><\
strong>The Girl with Only Lesbian Friends</strong></span></p>\
\
<p>*Doesn&#8217;t exist in the state of nature.*</\
p>\
<p><span style="text-decoration:underline;"><strong\
>The Girl with a Mixed Group of Girl and Guy Friends</strong></\
span><br />\
LTR potential: Be careful,  your player days might be\
over with her!<br />\
Chance of mental instability: She makes most girls\
seem like candidates for institutionalization</p>\
<p>And here we have\
the ideal girl,  if LTRs are your thing. (Note: If same\
night lays are your thing,  she is NOT the ideal girl.) She\
is open-minded and humble enough to enjoy the company of a variety of\
friends with strong opinions,  she has enough femininity to relish\
time with girl friends\
,  and she has enough exposure to guy friends that she can\
sympathize with their\
concerns. Ideal scenario: her girl and guy friends are all in\
relationships of\
their own. This limits the cattiness and the beta orbiter supplication\
to a manageable\
level.</p>\
<p>A girl who maintains an attractive humility and\
who respects the wishes and the laments of men is a girl who is emotionally\
secure enough to not just tolerate,  but embrace,  the company of both girl\
friends and guy friends. She loves people for who they are,  and not\
for what they can do for her ego.</p>\
<p><span\
style="text-decoration:underline;"><strong>The Girl with One or\
Two Player Friends</strong></span><br />\
LTR potential: bimonthly tests\
for STDs,  OR GF material<br />\
Chance of mental instability: She\
&#8217;s not crazy,  she&#8217;s creative!</p>\
<p>If a girl spends a lot of time with either a Samantha\
-type slut or a Hitch-like player,  she&#8217;s\
got hang-ups about her sexuality and her dating market value worth. She\
wants to live vicariously through their exploits because she herself\
lives a rather modest life\
,  or she IS like them and enjoys being with people who live and think\
just as she does. If the former,  she might be redeemable with enough\
LTR game. If the latter,  there&#8217;s a good chance\
that eerie suspicion you had that she was getting pounded by another\
cock last Thursday\
was true.</p>\
<p>Major red flag: Double all her\
slut points if the time she spends with the player or the slut is over\
Sunday brunch at a tapas restaurant,  getting drunk on mimosas.</p>\
<\
p>***</p>\
<p>My hope with this post is to impress\
upon the male reader the importance of not only screening girls\
for LTR potential,\
but of winning over a girl&#8217;s friends,  man or woman\
,  if you intend to date her beyond the customary three weeks. While it\
appeals to a certain renegade male mindset to boff a girl and pay no heed\
to her extraneous social life,  it&#8217;s always better to have\
her friends on the inside of the tent pissing out,  than outside pissing in\
. Girls,  being the lemming sex,  rely more heavily than men do on\
the judgment of their friends&#8217; opinions about their boyfriends. If she\
is someone you could date for the long haul,  best to befriend her social\
circle eagerly. If nothing else,  you have neutralized any future\
sabotage. More\
likely,  you have made a new group of friends. And if your girlfriend\
is cool,  then the solid bet is that her friends are cool,  too\
.</p>\
'


c14 = epub.EpubHtml(title='age brackets',
file_name='age_brackets.xhtml',
lang='en')
c14.content='\
<h2>The Difficulty of Gaming Women by Age Bracket</h2>\
<\
p>The following observations apply to established adult men,\
post college years.\
Younger men still in college will find their success rate with\
women of various ages\
,  particularly older women (aka cougars),  highly variable.\
The rules for them\
will be different than the rules for older men.</p>\
<p><\
strong><span style="text-decoration:underline;">18 to 22 year\
olds</span></strong></p>\
<p>Hard to believe,\
but it is often easier to bed a very young woman than an older woman\
,  if you are an older man. This is because 20-40%\
of women are specifically attracted to older men. It is hard-wired in\
them,  and this hard-wiring can be reinforced by poor\
family upbringing resulting\
from divorce of parents or absentee fathers. Single moms are\
the greatest source of\
future generations of slutty daughters the world has ever known.</p>\
<p\
>Your goal is to identify which 18-21 year olds are amenable to\
being seduced by you. Since a majority will balk at the idea,  you\
should learn to quickly identify and NEXT! them. Thankfully,  most girls aren\
&#8217;t brazen cockteases,  and will make their lack of interest known\
early on. Beware,  though,  that a small minority of barely legal rapacious\
golddiggers will try to keep you on tenterhooks,  extracting\
your resources for little in\
return. A simple <a href="https://heartiste.wordpress.com\
/2008/09/16/how-to-handle-femmes-\
fatales/" target="_blank">preemptive qualification</a> should suffice to smoke\
them out.</p>\
<p>You can bang an 18-21\
year old surprisingly quickly because they have little ASD\
(anti-slut defense).\
This is because they do not have the long history of\
sluttiness common to older\
women which needs to be rationalized away by posturing as a paragon\
 of chaste virtue\
. A young woman simply won&#8217;t perceive sex with you as\
an admission of sluttiness. She is innocent to herself as well as to you\
. Plus,  actual slutty behavior has been defined down so that\
five partners today\
is equivalent to one partner thirty years ago.</p>\
<p>Caveat\
to the above: although you can get the bang with an 18-21\
year old very quickly,  you should not prime the path to banging with obvious\
signs of physical escalation. There is a high risk with very young women that\
escalating kino will be perceived as &#8220;pervy&#8221; or &#\
8220;creepy&#8221;. This means no PDA,  no &#8220;\
innocent&#8221; touching of her erogenous zones,  and no raunchy sex talk\
. You want to keep it on the superficial friend tip until she is in\
your place. Then you should escalate rapidly. You&#8217;d be\
amazed how fast the young woman sheds her clothes when the bang is in sight\
. Very little foreplay is required. The sex will be,  as you can\
imagine,  the <a href="https://heartiste.wordpress.com/\
2007/08/30/hotter-women-better-sex/" target\
="_blank">hottest you will ever have</a>.</p>\
<p\
>DO NOT EVER &#8220;DATE&#8221; an 18-21\
year old. Women under 23 don&#8217;t date,  they &#\
8220;hang out&#8221;. Anything that remotely smacks of a date &#\
8212; drinks at a lounge,  dinner for two,  day trips to a\
museum &#8212; will scare her off. The under-23 young woman\
cannot handle the &#8220;seriousness&#8221; of a dating context.\
This is the reality of modern America. &#8220;Dating&#8221;\
makes younger women think &#8220;no fun,  marriage,  kids,  pressure\
,  relationships,  stuff that older people do&#8221;. You need to be\
so chill that you&#8217;re barely motivated to do anything proactive with\
her. Instead,  &#8220;hang out&#8221; with her in\
a neutral context. Walks along window-browsing streets are good for this.\
So is meeting at a local park and talking while goofing off on the swings\
. You can take her to a coffee shop as long as you don&#\
8217;t buy anything.</p>\
<p>DON&#8217;\
T BE LAME. If a 19 year old (true story) offers you\
an E tab in a dark corner of a loud club at 1 am,\
don&#8217;t refuse her like some boring fuddy duddy. Either pop\
that baby and enjoy the ride,  or pretend to take it and throw it\
away when she&#8217;s not looking if you&#8217;re\
suspicious of the pill&#8217;s origins and purity. Push for a\
blowjob in the alley behind the club; plans to make future dates are a\
fool&#8217;s errand.</p>\
<p>DON&#8217\
;T BE HER DAD. Contrary to popular misconception,  most young women don\
&#8217;t want to date a father figure. They DO want to\
date a strong dominant man,  and older men bring that demeanor to the table\
. This is why it is better to dress youthfully (if you are in\
shape) rather than in a sharp suit and tie if it&#8217\
;s much younger women you want to meet. A notable minority of younger\
women love the business suit look,  but most of them,  especially the ones\
on the fence about dating older men,  would feel more\
comfortable if you projected\
an aura of youthfulness through your dress and attitude.</p>\
<p><\
strong><span style="text-decoration:underline;">23 to 27 year\
olds</span></strong></p>\
<p>Similar to the 18\
-22 year olds in terms of difficulty of picking up,  with some important\
differences. The 23-27 year old feels she is at her attractiveness peak\
,  despite her peak having passed a few years earlier. This is because she\
is surrounded by many more high status men than she was while in college (\
    or working at the Piggly Wiggly) who are expressing sexual interest in her\
. This social dynamic will work to inflate her ego beyond the bounds of her\
actual beauty ranking. Some consequences result from this.</p>\
<p>\
NEG HARDER. The 23-27 year old will require harder negging than any\
other age group of women,  even the hotter 18 year olds. She needs\
her ego punctured before her pussy will open for you.\
Remember that cherished maxim\
:</p>\
<p><strong>Maxim #23: The defensive crouch\
is where pussy tingles are born</strong>.</p>\
<p>DEFY\
EXPECTATIONS. She expects you to pay her way and play the role of earnest\
suitor. You can&#8217;t &#8220;hang out&#8221\
; with the 23-27 year old like you should with the 18-\
22 year old without staining yourself with the immaturity label,\
but you shouldn&#\
8217;t fall into her trap of arid,  sexless dating either. Arrange\
dates that are simple and logistically favorable. Never spend\
 more than two drinks&#\
8217; worth of money on her on a single date.</p>\
<\
p>DATE CONCURRENTLY. The 23-27 is,  arguably,  the most\
in-demand woman on the market. Various social factors account for this,\
which will be the subject of another post. Thus,  she will have the\
greatest self-regard. Despite your best game,  you may find yourself getting\
flaked on by a girl in this age range. A good defense is a\
solid offense,  so minimize the creep of neediness and\
desperation by dating many women\
at once. Do not feel guilt about fucking multiple women concurrently.</p>\
\
<p>THIS IS YOUR SWEET SPOT FOR GAME. No other woman will\
react as positively to hardcore game as the 23-27 year old. She\
and her sisters will be throwing meatballs at the middle of your lineup. Aim\
for the fences.</p>\
<p><strong><span style="text\
-decoration:underline;">28 to 30 year olds</span></strong></\
p>\
<p>Finally,  the female ego suffers chinks in its armor\
. She will try hard to cover these cracks,  but they&#8217;\
ll creep out here and there. 30 is a huge and depressing milestone for\
women,  but 29 is an even more depressing birthday. It is the &#\
8220;last hurrah&#8221;,  so to speak,  and the number taunts\
her daily with reminders of her impending obsolescence. A\
single girl who was dumped\
by her boyfriend and who has just turned 29 may be the easiest girl in\
the world to lay. You will still need to game her,  but the\
path to sex will be exhilaratingly fast and furious.</p>\
<p>\
28-30 year olds are a mixed bunch. Some are riding a wave\
of career and social success that has nowhere to go but down,  and their\
bloated egos reflect that. Others,  less conventionally\
successful,  are emotionally frazzled by\
the disappearing act of their heady youth and by\
the intractability of their singledom.\
You will find some of the cuntiest,  and sweetest,  girls in this age\
range.</p>\
<p>Same rules as the ones for 23-\
27 year olds apply to 28-30 year olds,  with the exception that\
negging should be tailored to the life success as well as the looks of the\
girl you are gaming. A 30 year old businesswoman is often harder to game\
than a 20 year old hipster. She will need subtle reminders that her beauty\
isn&#8217;t what it once was.</p>\
<p><\
strong><span style="text-decoration:underline;">31 to 34 year\
olds</span></strong></p>\
<p>In some ways,\
women in the 31-34 age range are the toughest broads to game.\
(By &#8220;toughest&#8221;,  it is meant &#8220;\
 most time consuming&#8221;.) It&#8217;s counterintuitive,  yes\
 ,  but there are factors at work besides\
 her declining beauty which mitigate against\
 the easy,  quick lay. For one,  it is obviously harder to\
 meet single 31-34 year old women than it is to meet single\
 younger women. Marriage is still a pussy-limiting force to contend with\
 for the inveterate womanizer,  but Chateau apprentices are hard\
  at work battling the\
 scourge of mating market disturbances caused by the grinding and\
  churning of the marriage\
 machine.</p>\
<p>But the bigger reason 31-34\
 year olds are harder to game than any other age group of women has\
 to do with the wicked nexus of entitlement and\
 self-preservation that occurs\
 at this age in women. When you combine a disproportionate\
sense of entitlement\
 fueled by years of feminism,  steady paychecks and\
 promotions,  and cheerleading <\
 a href="https://heartiste.wordpress.com/2009/04\
 /20/your-gay-doom/" target="_blank">gay\
 boyfriends</a> with suspicions of every man&#8217;s motives\
 and a terrible anxiety of being used for a\
  sexual fling sans marriage proposal\
 ,  you get a venom-spitting malevolent demoness on guard against anything she\
 might perceive as less than total subjugation to her craving for\
 incessant flattery and\
 princess pedestaling.</p>\
<p>Note that Chateau guests aren&#\
 8217;t necessarily complaining. A harder-to-game 33 year\
 old is kind of like getting bumped down from a Honda Civic rental but\
 driving off the lot with the consolation prize of a Ferrari.</p>\
\
 <p>Listen to any man who is good with women and they\
 will tell you the same thing:</p>\
<p>&#8220;\
 I have an easier time bedding and dating 23 year olds than I do\
 33 year olds.&#8221;</p>\
<p>This defies all\
 logic until you see it through the eyes of the hamster sweating its fluffy\
 ass off in a woman&#8217;s brain. (Poor little\
 creature must be pooped out by the mid-30s.) Sure,  a\
33 year old is not as hot as the 23 year old version of herself\
,  but her ASD is through the roof,  as is her self-conception\
as a hot marriage-worthy commodity. Many older women will tell themselves that\
their experience,  maturity,  accomplishments and financial stability mean\
they should be way more\
valuable to men seeking wives than some young babe on the take. Of course\
,  they have to tell themselves this because reality isn&#8217;t making\
it easy to believe.</p>\
<p>These are the kind of\
women who have sexual flings with college guys,  because they\
can psychologically box those\
men in as &#8220;purely for fun&#8221; adventures. But\
the men the 31-34 year old women really want are the older,\
established men who will give them a marriage proposal and a family. This is\
why it is counterintuitively harder to game the older woman who\
still retains a vestige\
of her youthful attractiveness: she wants and expects so much\
more than the younger\
woman.</p>\
<p>Game required: Strong body language,  masculine\
dominance,  sharp suits and shoes,  easy on the negs and palm reading,\
emphasis on the comfort stage,  lots of travel stories,\
disqualify yourself from sex\
on the first date,  <a href="https://heartiste.wordpress.\
com/2009/01/29/vulnerability-game/" target="_blank\
">vulnerability game</a>,  avoidance of the beta provider zone.</p>\
\
<p>In short,  if you can present yourself to her as different\
than the indistinguishable mass of sad schlumpy <a href="https://heartiste.\
wordpress.com/2010/05/19/beta-or-herb\
/" target="_blank">beta herbs</a> who are her typical choice\
in available men,  then you are guaranteed the lay. Just don&#8217\
;t expect to sleep with her on the first night. She will work\
hard to make your seduction as difficult and drawn out as possible.</p>\
\
<p>Note: DO NOT SPEAK OF THE YOUNGER WOMEN YOU DATE to\
an older woman. You will be tempted to do this to demonstrate your higher\
value,  but instead she will withdraw so fast into her ego-preserving turtle\
shell that no game will redeem the pickup. If the subject comes up,\
just tell her you&#8217;ve &#8220;dated many interesting women\
&#8221; and leave it at that.</p>\
<p><strong\
><span style="text-decoration:underline;">35 year olds</span\
></strong></p>\
<p>This age gets a special mention.\
Why? Because 35 is the year of formal female expiration. (Informal expiration\
can occur many years later,  depending on the woman&#8217;s\
genetic\
good luck.) At 35,  most women are over the hill.\
An\
unmarried woman at 35 is officially in crisis mode. Full meltdown will happen\
within\
the year if she isn&#8217;t hitched in that time.\
You\
do not want to be in the vicinity of a woman in full meltdown mode\
. Full meltdown is accompanied by the acquisition of a second\
cat,  alcoholism,\
cackling brunches of mimosas with equally pathetic Samantha wannabes,\
sloppy drunken one night stands\
with college age men which they will then rationalize as evidence\
of their enduring beauty\
,  and a laundry list of annoying personality tics and neuroses that\
would comfortably provide\
for the retirement plans of ten psychotherapists.</p>\
<p>Game required\
: &#8220;Hi&#8221;.</p>\
<p><strong><\
span style="text-decoration:underline;">36 to 38 year olds</\
span></strong></p>\
<p>She is at peace with her\
spinsterhood and her failure in the dating market. She will acquiesce\
easily and gratefully\
to sex with very little game,  as long as you don&#8217;\
t look like a grandpa. Her expectations are so low,  it will be\
a challenge to disappoint her.</p>\
<p>If you are prone\
to guilt,  you might feel it when you inevitably dump a woman in this\
age range. Don&#8217;t. Remind yourself that her past is\
littered with her insouciant dumping of many beta\
men before you. You are merely\
an alpha agent of righteous karma.</p>\
<p>A Chateau proprietor\
once dated a European 37 year old for a couple of months. She looked\
years younger than her age,  so the sex was fun and the time together\
was relaxed,  but everything was glazed with a tint of sadness. A vow\
was made never to go much above 30 again.  So far,  the vow\
remains unbroken.</p>\
<p><strong><span style="text-\
decoration:underline;">39+ year olds</span></strong></p>\
\
<p>No Chateau proprietor has experience dating or fucking women 39 years old\
or older,  so we cannot offer much advice for gaming women in this age\
range. Yes,  yes,  we can all hear you crying now.</p\
>
'




c15 = epub.EpubHtml(title='the wall',
file_name='the_wall.xhtml',
lang='en')
c15.content='\
<h2>The Wall</h2>\
<p><strong>the wall</strong> [thuh wawl] <\
em>-noun</em>: 1. a large,  immovable monolith of frightening\
and awesome power capable of threshing egos and rending souls,\
serving as a metaphorical\
stoppage point at the intersection between a woman&#8217;s declining\
 sexual attractiveness\
and her advancing years,  beyond which female sexual\
desirability disappears into the misty void\
.</p>\
<p><a href="http://www.futurepundit.\
com" target="_blank">FuturePundit</a> has a post up <\
a href="http://www.futurepundit.com/archives/006914.\
html" target="_blank">highlighting a scientific study</a> which concludes\
,  most depressingly,  that by age 30 only 12% of a woman&#\
8217;s eggs remain.</p>\
<blockquote><p>Tom Kelsey\
,  a Senior Research Fellow at the School of Computer Science at St Andrews,\
said,  &#8220;Previous models have looked at the decline in ovarian reserve\
,  but not at the dynamics of ovarian reserve from\
 conception onwards. Our model\
shows that for 95% of women,  by the age of 30 years,\
only 12% of their maximum ovarian reserve is present,  and by the age\
of 40 years only 3% remains.</p></blockquote>\
<p>\
This is a surprise even to me. I knew there was a significant dropoff\
in female fertility by age 30,  but I didn&#8217;t know\
it was this precipitous. I find this news depressing,  because\
female fertility and\
sexual attractiveness closely parallel; allowing for a few lag years\
for the outer shell\
to catch up to the inner biology,  the number of viable eggs a woman\
has remaining directly correlates with the number of years she has\
 left as a highly\
coveted product on the sexual market. That is,  when a woman has a\
full basket of eggs she is at her most beautiful. When she has dwindled\
to 50% eggs left,  she is desireable to only half the men she\
was capable of attracting for short and,  particularly,  long\
term relationships when she\
was at her beauty prime. And when she is down to 3% eggs\
at age 40,  she can only attract 3% of the men she used\
to attract for long term investment when she was peaking at,  typically,  age\
20. And what&#8217;s worse,  those 3% of men\
are the leftover omega dregs with no other options whom she turned\
down when she\
was a hotter commodity.</p>\
<p>Personally,  as a man\
who has no desire to have kids,  the number of remaining eggs a woman\
has left is of no concern to me other than as an abstract matter.\
But a woman&#8217;s beauty is of paramount concern to me,\
and as such it would happen that,  through the use of my infallible divining\
boner rod,  my very selective screening procedures against\
women showing signs of physical decay\
would necessitate that I avoid dating women with less than 50% eggs in their\
basket. So far,  this is how it has worked out,  and I\
&#8217;ve mostly game and a devilish smile to thank for that.</\
p>\
<p>This saddens me. Why? I will explain.\
Anything,  any uncontrollable force,  that strips beauty from the\
 world is my enemy\
. How much grander and pleasurable life if women stayed beautiful\
for 100 years instead\
of a precious 15 years? How much love would my heart shout at the\
world if the pool of beautiful women was every woman,\
everywhere,  forevermore,\
and not just a small sliver of women with power so fleeting it may as\
well be a curse than a blessing? Imagine this world,  and tell me\
then how you keep the demons of hate from lashing impudently and\
futilely against the\
natural order of things. I say fuck the natural order. Bring on the\
life and beauty extending tamperings of human ingenuity. Get off\
your knees,  you\
limp-noodled gaiaists and blithely stoic servants of religion,\
you philosophical naifs and\
self-deluded sophists. Turn the tables and bring your\
evolutionary inheritance to its\
knees,  if you dare.</p>\
<p>More evidence for the\
wall comes from a <a href="http://www.dailymail.co\
.uk/femail/article-1246576/You-CAN-old-\
overnight.html" target="_blank">Japanese study showing that there is a\
real &#8220;tipping point&#8221; in aging</a>,  or\
a &#8220;hitting the wall&#8221; effect,  where a woman\
&#8217;s natural biological ability to rejuvenate herself and stay toe to toe\
with the ravages of aging slips into freefall at age 35,  much younger than\
previously thought.</p>\
<blockquote><p>&#8216;While some measurements showed a gradual decline,\
cheek volume &#8211; one of the key factors in a youthful appearance &#\
8211; can drop off suddenly,  by as much as 35 per cent in\
a year, &#8217; he says.</p></blockquote>\\
<p\
>Naturally,  there are some women whose stress-inducing lives of stripping,\
smoking,  slutting,  and single motherhood age them much faster\
than their actual years\
. These are truly tragic cases,  for they have thrown away\
their most precious\
asset for instant gratification.</p>\\
<p>In other news,  the\
new HBO documentary &#8220;<a href="http://www.hbo.\
com/documentaries/youth-knows-no-pain/index.html\
" target="_blank">Youth Knows No Pain</a>&#8221; was\
pretty good. A number of the women interviewed were boldly honest\
about their declining\
sexual attractiveness,  and the reasons for why they went\
under the knife to &#\
8220;get a little work done&#8221;. One woman even noted that\
when her friends told her there are plenty of women who look good for their\
age,  like Sophia Loren,  she responded that Sophia Loren is just one woman\
out of millions who &#8220;don&#8217;t look so good\
when they get older&#8221;. Found: A woman with a grasp of\
basic statistical concepts. Alert the media!</p>\\
<p>Most of\
the women in the documentary looked like alien-eyed stretchy gumbo toys,  but\
a couple did actually look pretty good,  at least ten years younger than their\
ages. At some point,  the science is going to have to dispense with\
the scalpel and start rejuvenating under the hood,  fixing\
the problem at its source\
using stem cells or some other form of cellular manipulation. I can&#8217\
;t wait for matrix-like abortion mills to be constructed to help my\
harem stay young and sexy for as long as possible.</p>\
'


c16 = epub.EpubHtml(title='boredom',
file_name='boredom.xhtml',
lang='en')
c16.content='\
<h2>Time to Boredom</h2>\
<p>There are two\
reasons men get bored with women\
: Intellectual incompatibility and beauty incompatibility\
. The less mentally stimulating or\
aesthetically stimulating a woman is to\
\
a man,  the quicker he\
will grow bored with her and\
throw his worm\
back into the\
waters for nibbles from new fish\
. Which of these two factors\
\
controls a larger portion of a\
man&#8217;s interest\
? Beauty,\
clearly,  and\
especially so in the critical first\
few months,  but assuming a\
\
threshold for acceptable beauty is met\
intellectual attraction or lack thereof serves\
to capture a\
man&#8217\
;s interest beyond the three\
-month mark. If neither\
\
the beauty nor intellectual threshold of\
attraction is crossed,  a man\
will get bored\
after the first\
ejaculation. If both are met\
,  a man is susceptible to\
\
the woman&#8217;s\
ploys to entrap him into marriage\
.</p>\
\
<p\
>Beauty and intellectual compatibility are\
relative to the man&#8217\
;\
s dating market value.\
If the man is a 9\
,  he will need\
a woman\
who is a 9 or 10\
in beauty,  and no less\
than\
10 IQ points lower than\
his own,  if he is\
to avoid getting bored\
with her\
after a month or two.\
Although I&#8217;ve\
known\
plenty of people whose wit\
,  charm,  and humor belied\
their average IQs,\
I will\
use IQ in this post as\
a rough proxy for intellectual and\
personality\
compatibility. For purposes of\
discussion,  I&#8217;\
ll set aside the\
few exceptions\
where the IQ of the partners\
is equal but their interests are\
so\
contrary that boredom becomes a\
manifestation of despising the other person\
&#8217;s\
hobbies.</\
p>\
<p>What\
follows is a handy chart illustrating\
<\
strong>Time To Boredom\
</strong> for the average\
man (male dating\
                                                     value rank\
     = 5 on a scale\
     of 0 &#8211;\
     10 inclusive\
                                                     ) based on\
the two critical variables of female\
beauty and IQ. Note\
that\
Time To Boredom is a relative\
value that will,  on average\
,  occur\
much sooner for a\
high ranking man than it would\
for a low ranking man\
.\
It is conceivable,  in fact\
,  that a male 10 will\
get bored\
with every woman he\
meets within hours if he doesn\
&#8217;t have\
mistresses\
to take up the slack in\
his attention span,  while a\
male zero\
might take years to\
get bored of a female zero\
,  although in the latter\
case\
the boredom might be just as\
quickly forthcoming but given the dearth\
of options\
available to the male zero he will work hard to keep his boredom and disgust\
hidden from his ugly partner.</p>\
<p>Female IQ is measured\
against a male baseline of 100.</p>\
<p>Female Hotness            Female\
Time To Male<br />\
\
<span style="text-\
decoration:underline\
;">Rank </\
span> <span style="\
text-decoration:underline;">\
\
IQ </span> <span\
style="text-decoration:\
    underline;">Boredom\
</span\
><br />\
0                                   +-10\
points     1 nanosecond (Neural disgust\
                         registers\
                                                                  <br />\
before\
                         conscious awareness)<br />\
\
0                                   &gt;-10\
points\
same diff<br />\
0\
&gt;+10 points     same\
diff<\
br />\
1                                   +-\
10 points      1 millisecond (time\
                              to retinal burn)<br\
\
/>\
1                                   &gt;-10\
points      irrelevant<br />\
1\
&gt;+\
10 points     1 millisecond to boredom + annoyance<br />\
2                                   +-10 points\
1 second<br />\
2\
&gt;-10 points      1\
minute (male\
                                                                  inspired to<\
        br />\
ridicule the dummy\
        )<br />\
2                                   &\
gt\
;+10 points     1 minute\
(male inspired to<br\
 />\
ridicule the nerd\
                          )<\
br />\
3                                   +-10 points\
5 minutes (male tries to\
           find\
                                                                <br />\
redeeming\
           quality)<br />\
3\
&gt;-10 points\
3\
minutes (male fails at finding\
         <br />\
redeeming quality\
         )<br />\
\
3\
&gt;+10 points     6\
minutes (takes male extra minute\
         to<\
                                                                  br />\
realize\
         she&#8217;s\
         ugly thanks to her<br />\
impressive knowledge of<br />\
computer hardware)<br />\
4                                    +-10 points      1 hour \
(male wants same night lay\\
 )<br />\
4                                    &\
gt;-10 points      1/\
2 hour (male wants same \
        hour lay)<br />\
\
4                                    &gt;+10 points\
\
2 hours (males wants same\
         \
         night lay<br />\
\
\
\
         with talky talky chick\
         )<\
\
br />\
5                                    \
+-10 points\
5 weeks (\
    bloom off the\
         rose after<br />\
\
         third bang)<br />\
\
5                                    &gt;-10 points\
3 weeks (pillow talk excruciating\
         )<br />\
5                                    &\
gt;+10 points     4 weeks\
(male charmed,  then annoyed\
 , <br />\
by\
 chick&#8217;s\
 nerdiness)<br />\
6\
+-10 points      3 months (\
    best he&#8217;\
    s ever had, <\
    br />\
but still not\
    that good)<br />\
\
6                                    &gt;-10 points\
2 months (her hobby is\
          <a href="https\
          ://heartiste.wordpress.\
          com/2008/05\
          /30/flip-\
          cup-game/" target\
          ="_blank">beer pong\
          </a>)<br />\
\
6                                    &gt;+10 points\
2.5 months (emasculated\
            by her<br />\
\
            sharp tongue)<br />\
\
7                                    +-10 points      1 year\
(a beta&#8217;\
 s heaven)<br />\
\
7                                    &gt;-10 points\
9 months (tard kills boners\
          dead)<br />\
7\
&gt;+10 points     1\
.5 years (male inspired\
          by her, <br\
          />\
but relationship unstable)<\
br />\
8                                    +-10 points\
5 years (even a beta\
         will get tired<br\
         />\
of sex with same\
         hottie)<br />\
8\
&gt;-10 points      5\
years (she&#8217;\
       s too hot to care\
       <br />\
about tardness\
       )<br />\
8                                    &\
gt;+10 points     5 years\
(she&#8217;s\
 too hot to care<\
 br />\
about nerdiness)<\
br />\
9                                    +-10 points\
30 years (beta suffers seizure\
          from<br />\
constant\
          stream of endorphins)<br\\
/>\
9                                    &gt;-10\
points      30 years (she&#\
                      8217;s too hot\
                      to notice<br />\
\
                      tardness)<br />\
9\
&gt;+10 points     30\
years (she&#8217;\
       s too hot to notice\
       <br />\
much of anything except<br />\
how hot she is)<br />\
\
10                                 +-10 points      forever (\
    entered realm of unreality)<\
br />\
10                                 &gt;-\
10 points      forever + 1 (\
    tardness means she can&#\
    8217;t<br\
    />\
tell he&#8217\
    ;s a beta)<\
br />\
10                                 &gt;+\
10 points     forever -1 (\
    one day,  she uses\
    big word<br />\
\
    that renders him impotent)</\
p>\
<p>As\
you can see,  it is\
almost guaranteed that men of every\
status rank will grow bored with\
their girlfriends,  dates,  wives\
,  fuckbuddies without an external injection\
of groinal stimulation. There is\
only one way a man can\
delay Time To Boredom:</p>
'


c17 = epub.EpubHtml(title='quality vs quantity',
file_name='quality_vs_quantity.xhtml',
lang='en')
c17.content='\
<h2>Quality VS Quanity\
,  Formula Version</h2>\
\
<p>Ah,  that\
perennial conundrum. That gavel of\
masculine judgment. Does the quality\
or the quantity,  or both\
,  of women that a man\
beds determine his alpha mojo?\
The hosts have graciously elaborated on\
this topic <a href="\
https://heartiste.wordpress.\
com/2008/05/\
02/quality-vs-\
quantity-pussy/" target="\
_blank">in the past</\
a>,  which should have been\
the final word,  but not\
all of the world&#8217\
;s 7 billion people have\
yet stayed a night at the\
Chateau to wake in the morning\
infused with the knowledge of the\
Celestials.</p>\
<blockquote\
><p>Any guy who\
claims to have game but picks\
up hundreds of circus freaks a\
year will be a laughingstock.\
And the boastful guy with few\
notches who claims to know everything\
about women because he’s\
been dating his cute high school\
sweetheart his whole life will similarly\
be mocked.</p></blockquote\
>\
<p>To put\
it in logical terms easily grasped\
by the aspies among us (\
    first number in each series\
    refers to penis-in\
    -vagina notch count unless\
    otherwise noted; second number\
    refers to female attractiveness rating\
    on a 0-10\
    scale):</p>\
<\
p>Stiff autumn breeze &\
lt;more alpha than&\
gt; 100 0s</p\
>\
<p>Unlubed masturbation\
&lt;more alpha than\
&gt; 100 hundred 1s\
&lt;more alpha than\
&gt; 200 0s</\
p>\
<p>Couch\
crease &lt;more alpha\
than&gt; 100 2s\
&lt;more alpha than\
&gt; 200 1s &\
lt;more alpha than&\
gt; 300 0s</p\
>\
<p>Lubed masturbation\
&lt;more alpha than\
&gt; 100 3s &\
lt;more alpha than&\
gt; 200 2s &lt\
;more alpha than&gt\
; 300 1s &lt;\
more alpha than&gt;\
400 0s</p>\
<\
p>Barely legal porn-\
assisted masturbation &lt;more\
alpha than&gt; 100\
2s &lt;but less\
alpha than&gt; 100\
3s over a two month time\
span</p>\
<p\
>Handjob by a 4 &\
lt;more alpha than&\
gt; 10 3s</p\
>\
<p>Blowjob by\
a 4 &lt;more\
alpha than&gt; 15\
3s</p>\
<p\
>Chandelier swinging,  titty fucking\
,  throat gagging,  motorized defiling\
,  publicly violating,  video recorded\
facialized money shotting,  post-\
coital sammich making,  never see\
her again sex with a 4\
&lt;more alpha than\
&gt; 50 missionary style\
3s</p>\
<\
>Fleeting glance from a 10\
&lt;more alpha than\
&gt; 100 1s</\
p>\
<p>Handjob\
by a 10 &lt;\
more alpha than&gt;\
\
1, 000 1s</p\
\
>\
<p>Blowjob by\
\
a 10 &lt;more\
\
alpha than&gt; 10\
\
, 000 1s</p>\
\
\
<p>Sex with\
a\
10 &lt;more\
alpha\
than&gt; 100\
,\
000 1s</p>\
\
<\
p>Anal sex with\
a\
10 &lt;more\
alpha\
than&gt; Infinity\
1s\
</p>\
<p\
>\
100 5s &lt;\
more\
alpha than&gt;\
100\
4s &lt;more\
alpha\
than&gt; 500\
3s\
</p>\
<p\
>\
50 6s &lt;\
more\
alpha than&gt;\
100\
5s</p>\
<\
p\
>40 7s &lt\
;\
more alpha than&gt\
;\
100 6s</p>\
\
<\
p>30 8s &\
lt\
;more alpha than&\
gt\
; 100 7s</p\
>\
\
<p>10\
9s &\
lt;more alpha\
than&\
gt; 100 8s\
</p\
>\
<p>\
1 10\
&lt;more\
alpha than\
&gt; 3\
9s</\
p>\
<p\
>LTR\
with a 10 &\
lt;\
more alpha than&\
gt;\
one night of sex\
with a\
10 &lt;\
more alpha\
than&gt;\
LTR with\
an 7</p\
>\
<\
p>One night\
of sex\
with a 9 &\
lt;\
more alpha than&\
gt;\
Rotating harem of multiple\
LTRs with\
100 5s and 6s\
&lt\
;more alpha than\
&gt\
; One night stands\
with 1\
, 000 4s</\
p>\
\
<p>\
LTR with a\
0 &lt\
;more alpha\
than&gt\
; Nothing</\
p>\
<\
p>Serial\
LTRs with 5\
10s &lt\
;more alpha\
than&gt\
; One night\
stands with 100\
9s &lt\
;more alpha\
than&gt\
; Lifelong monogamous\
LTR with an\
8</p\
>\
<p\
>Unmarried,\
cohabiting,  child\
-free,\
sex-gorged\
LTR with an\
8 &lt\
;more alpha\
than&gt\
; Once-\
a-month\
married sex with\
a 9 &\
lt;more\
alpha than&\
gt; Once\
-a-\
day married sex\
with a 7\
</p>\
\
<p\
>Unmarried,  commitment\
-free\
,  responsibility-absolved\
,  sex\
-on-demand\
with a\
cast of 1,\
000s of faithful 10s wearing kneepads\
and schooled in the culinary arts\
&lt;more alpha than\
&gt; The universe</\
p>\
<p>***</p\
>\
<p>So,\
if you have ass-banged\
one 10 in your life,\
you have equivalent bragging rights to\
the guy who has banged every\
1 in the world.</p\
>\
<p>If you\
have effortlessly banged 10, 000\
1s,  you have less bragging\
rights than the guy who has\
gotten one (freely given)\
blowjob from a 10. If\
you needed to expend huge effort\
to bang those 10, 000\
1s,  you have less bragging\
rights than the guy who stuck\
it in a couch crease for\
quick relief.</p>\
<\
p>If you have inspired\
a 6 to want a relationship\
with you,  you have more\
alpha bragging rights than the guy\
who has inspired 10 4s to\
spread their legs for him.</\
p>\
<p>Where\
it gets blurry is in the\
plain middle of the beauty arc\
. A guy who banged one 6 technically will\
be more alpha than the guy who banged two 5s,  but at those fine\
gradations,  who&#8217;s really keeping tabs? That&#8217;\
s where <a href="https://heartiste.wordpress.com/2010\
/12/16/predicting-a-girls-infidelity/" target="\
_blank">the Template</a\
> will influence the grading curve and make distinctions\
harder to delineate.</p>\
<p>Ultimately,  the essence of alpha\
maledom all comes down to inspiring\
beautiful women to,  first and\
foremost,  desire\
your poundage,\
and then to desire your continual\
poundage,  and finally to desire\
\
your love. If you can\
seduce a hot babe into bed\
multiple times,\
then seduce her\
into love,  and then do\
this same thing with many hot\
babes over the course of your\
life,  you are an alpha\
male,  no matter what else\
you have or have not accomplished\
in your life. Many will\
balk at this,  but that doesn&#8217;t change its truth.</p>\
'

c18 = epub.EpubHtml(title='wrapped',
file_name='wrapped.xhtml',
lang='en')
c18.content='\
<h2>Wrapped Around His\
Finger</h2>\
<p\
>We talk a lot about\
alpha males here,  and their\
mysterious\
pull on women. We\
discuss their attributes,  their attitude\
and their game,\
and how\
and why it works to vibrate\
vaginas all across the land.\\
But\
sometimes the weight of theory\
can deaden the senses,  and\
it helps to have\
a real\
-life,  flesh and blood\
exemplar of alphaness staring you in\
the\
face to bring that theory\
down to solid earth,  where\
you can see and\
hear it\
all from your personal first-\
person view. In that spirit\
,\
I will relay a moment\
in time from my life so\
that you can feel\
like you\
&#8217;re stepping in\
my shoes and witnessing it yourself\
.</\
p>\
<p>\
I was at a large social\
event (the more\
astute readers\
       will be able to figure\
       out the type of event\
       from details\
in this post\
       ) and was seated at\
a table with mostly women &#\
\
8212; all in their mid\
to late 20s &#8212;\
and a couple\
of men.\
As a keen observer of sexual\
dynamics,  the rapport between one\
\
of the men and his girlfriend\
was especially entertaining to me.</\
p>\
<\
p>She\
was completely enamored of him,\
leaning against him,  smiling at\
\
him (and when she wasn\
     &#8217;t smiling\
     she was &#8220\
;\
     smizing&#8221; at\
     him  &#8212; smiling\
     with her eyes\
),  touching\
him on his hands and arms\
and shoulders and thighs,  blushing\
\
periodically when he deigned to smirk\
at her (which wasn&#\
        8217;t\
often),\
flattering him,  imperceptibly nudging her\
chair closer to his,  nuzzling\
\
into his man-nook where\
pec meets armpit,  gazing up\
at his face\
(and I\
 do mean UP,  as\
 she would deliberately arch her\
 back and\
neck so that\
 her body was compressed in\
 the vertical and he was\
 looming\
over the top of\
 her head),  defending him\
when her girl friends were\
challenging\
him on something he said,\
and,  best of all,\
apologizing profusely\
for imagined slights that\
she believed she had accidentally committed\
against him. When she\
spoke\
,  either to him or to\
others in his company,  she\
sounded,\
not to put too\
fine a point on it,\
like a ditz. Yes\
,\
she was doing all this in\
front of about ten people,\
some total\
strangers to her.</\
p>\
<p>For\
his part,  he was\
behaving\
and speaking in almost the exact\
opposite manner as his girlfriend.\
He would\
sit straight,  neither\
leaning away nor into her,\
would speak in a heavy\
and\
deep monotone,  would rarely smile\
(and when he did it\
 was always\
a half-\
 assed &#8220;yeah\
 i&#8217;m\
 the\
douchebag you wish you\
 were&#8221; effort\
 ),  would only touch her\
\
when he was reaching around to\
grab her ass for a makeout\
,  seemed\
oblivious to her cloying\
flattery,  effected an air of\
imperturbable indifference,  showed\
little outward\
signs of affection for her except\
for the one time I caught\
\
sight of them absconding to what\
they thought was a private location\
,  occasionally\
spoke ill of her\
even to the point of insulting\
her,  never complimented\
her,\
looked straight ahead in the middle\
distance when she complimented him,\
\
never said &#8220;thank\
you&#8221; or &#\
8220;\
excuse me&#8221\
;,  never excused or &#8220\
;forgave&#8221\
; her\
when she was excessively apologizing to\
him (in fact,  he\
\
     seemed to relish her clumsy\
     supplication),  would sometimes insult\
her friends right in\
front of\
her,  would often command (\
    not ask) her to\
get\
him a drink,  and\
,  best of all,  flirted\
with other hot\
girls at the\
table.</p>\
<p\
>There was a telling\
moment\
of the nature of their relationship\
early in the night. She\
was\
giddy and excitable as she\
laughed with her girlfriends and some\
new arrivals,\
when it suddenly\
dawned on her that she had\
neglected to promptly introduce her\
boyfriend\
to everyone. (And by\
              promptly,  I mean not\
              more than\
three seconds had\
              passed before she caught herself\
              in this supposed irredeemable faux\
              pas\
.) Red-faced\
,  she humbly corrected herself.</\
p>\
<p\
>&#8220\
;Oh my god,  I\
&#8217;m so sorry\
\
!&#8221; she pleaded as\
she looked at him. &#\
8220;\
I&#8217;\
m so sorry! So sorry\
! I forgot to\
introduce you\
to everyone! Everyone,  this\
is [name],  my boyfriend\
\
.&#8221; Now semi-\
whispering to him,  &#8220;Sorry\
,  baby! Sorry.&#8221;</p>\
<p>His facial\
expression\
remained unmoved. A powerful pause\
heightened the awkwardness before he answered\
.\
&#8220;Don&#\
8217;t worry about it\
. I got\
it.&#8221\
; He then nods in the\
direction of the others.</\
p\
>\
<p>His vocal\
tone and expression are important here\
.\
It was not consolingly beta\
,  where the pitch rises on\
&#8220;\
worry&#8221\
; and descends to a loving\
shoulder rub on an elongated\
&#\
8220;I got it&#\
8221;,  as his eyes crinkle\
at\
the corners in reassurance.\
Nope,  it was more like\
a staccato,\
Draper-esque\
,  punch to the face,\
flatly delivered,  emotionless except\
for\
a hint of contempt,  which\
was noticeable in the way he\
commandeered\
the drama by addressing the\
table himself and refusing to glance\
at her as\
she effused with\
apologia.</p>\
<p\
>I watched admiringly.\
The\
other man at the table glanced\
at his feet nervously. The\
girls\
were a mix of hatred\
and arousal.</p>\
<\
p>This\
guy was the\
flawless encapsulation of the jerk.\
The dick. The narcissistic\
prick\
. All together now&#8230\
;</p>\
<p>\
The\
Asshole Hot Chicks Love.</\
p>\
<p>And\
she? She was\
the hot\
chick who loves an asshole.\
Every mannerism,  word and body\
shift\
&#8212; right down\
to the tiniest facial tic &#\
8212; telegraphed her\
absolute devotion\
&#8212; her ADDICTION &#\
8212; to her jerk boyfriend\
.</\
p>\
<p>\
Now some of you will parry\
with the usual gripes\
. But\
before you do,  know the\
following:</p>\
<p\
>\
She graduated from a top\
-tier Ivy. Her degree\
is in a numbers\
-related\
field. She is hot,\
a hard 8.5.\
Her\
body is worthy of a\
sacrificial fuckening. According to my\
sources,  when she\
isn&#\
8217;t with her alpha\
-squared asshole boyfriend,  she\
is\
one of the smartest,\
most put-together and confident\
girls in a room\
. The\
ditz act,  apparently,  only\
blossoms in his presence. Her\
girl\
friends are jealous of her\
even though they hate what she\
becomes when she&#\
8217;\
s with him. And the\
blow that I know will sting\
beta\
males the worst? She\
COULD have almost any man she\
wanted &#8212;\
good men\
,  solid company men,  respectable\
men of their communities &#8212\
;\
but she chooses to be\
with an arrogant renegade.</p\
>\
<p>\
And him\
? Decent looking. Easy on\
the eyes,  I suppose most\
women\
would say. Certainly not\
Hollywood looks. Not a big\
or muscular guy.\
Lean to\
the point of skinny. Edgy\
,  downscale style. (She\
                     showed\
up at this event\
                     poured into an exquisite cocktail\
                     dress. He arrived late\
\
                     with her,  wearing frayed\
                     designer jeans and an untucked\
                     tight flannel shirt over\
\
\
                     a white Hanes wifebeater that\
                     was showing through the top\
                     . Most of the\
\
\
                     other men were wearing suits\
                     .) He was short.\
Yes,  he might\
have been\
a half inch shorter than his gf. Unemployed.</p>\
<\
p>You read that right. He lost his [redacted] industry job\
six months ago and was living\
off her earnings. He has\
money,  but\
he doesn&#\
8217;t spend it because\
,  as he explained to me\
\
,  he&#8217;s\
saving it for a few years\
of fun-\
time travel.\
Whether he intends her to go\
with him or not is left\
\
to interpretation.</p>\
<\
p>None of this is\
new to me\
. I&#\
8217;ve met guys like\
him before. I&#8217\
\
;ve *been* that\
guy plenty of times,  when\
the mood strikes\
. I&#\
8217;m intimately familiar with\
the adoring love copping such a\
\
grotesque asshole alpha attitude inspires in\
women. There is no escaping\
that this is\
a reality of\
female sexual nature,  a powerfully\
harsh reality that sends shockwaves of\
\
disbelief and disillusion through the more\
tenderhearted of the inexperienced idealists.\
Some learn from\
what they see\
behind the curtain; others cocoon\
further into self-medicating platitudes\
\
.</p>\
<p>\
And what about the spectators?\
What did the\
men and women\
in attendance think of him,\
both those who knew and knew\
\
of him? From what I\
could glean,  the men were\
largely neutral.\
Some hated him\
(usually the biggest betas with\
 overbearing girlfriends),  some liked\
him\
(maybe not surprising,\
 the alphas and the omegas\
 were affable toward him),\
\
and most were willing to throw\
him under the bus in furtive\
conversation at the\
behest of their\
gossipy girlfriends.</p>\
<\
p>More pertinently,  how\
\
did the women &#8212;\
all of them well-educated\
urbanite professionals &#\
8212; feel about him?\
In his company,  they were\
girlish and borderline\
shy,  or\
self-conscious. Behind his\
back,  they were disparaging,\
\
complaining bitterly of the way he\
treats his girlfriend (bitterness was\
                       correlated with their\
closeness to\
                       her),  and constantly &#\
8212; I mean CONSTANTLY &#\
8212\
; working to install his\
ouster. I saw one girl\
drag her away so\
that she\
could introduce her to a man\
who,  unknown to her at\
the\
time,  was a handsome\
gay man.</p>\
<\
p>If you\
held any\
doubts that girl friends will not\
conspire against you should they find\
you\
unacceptable boyfriend material for their\
friend,  well&#8230;\
you can put those\
doubts to\
rest now.</p>\
<\
p>Of course,  none\
of\
their efforts worked in the\
least. He had been dating\
his girlfriend for many\
years,\
during which time he has cheated\
on her for months at a\
stretch\
with more than one woman\
. His cheating,  his aloof\
treatment of her,\
her friends\
&#8217; dispproval&#8230\
; none of it seemed to\
have\
dampened her love for him\
. Or her loyalty to him\
,  for as I\
learned from\
a trusted source,  she never\
,  not once in the sumptuous\
prime\
of her life when she\
had every excuse and rationale to\
do so,  cheated\
on him\
.</p>\
<p>\
Remember that the next time you\
hear\
of some whiny ho cheating\
on her beta boyfriend,  and\
rationalizing it by blaming\
it all\
on him.</p>\
<\
p>The professed hate the\
girls\
had for this asshole boyfriend of\
one of their friends,  and\
the wet glower\
in their eyes\
when they spoke of him,\
belied a primitive attraction. It\
\
was not the impassioned hate a\
man has for another man who\
has humiliated him\
,  or the\
withering hate a woman has for\
a weak ex-lover who\
\
now repulses her. When I\
heard them talk about him,\
their words ostensibly\
carried a payload\
of anger and disgust,  but\
it was a gossamer veneer;\
\
to a hardened pro of female\
codespeak like myself,  the dulcet\
harmonies of untamed\
curiosity sent their\
words aloft on a stanza of\
gina tingles. Listen closely,\
\
and you can hear the subliminal\
poetry asserting itself &#8212;\
&#8220;\
ode to why\
oh why do i hate this\
guy but feel like i do\
\
?&#8221;</p>\
<\
p>Interestingly,  there was\
one girl,\
a looker in\
every way and smart as tacks\
to boot,  whose loathing for\
\
the asshole boyfriend of her best\
friend seemed the most genuine.\
I say &#\
8220;seemed\
&#8221;,  because it may\
merely be the case that she\
\
was best at concealing her shameful\
intrigue. Whatever the true motivation\
,  I found\
her responses to\
him the most cutting. She\
was clearly aiming for the throat\
\
,  and her eyes pierced like\
laser beams,  her voice cold\
and still as\
sheet ice.\
Lesser men would have suffered a\
grievous wound from her attacks,\
\
for her barbs were sharp and\
subtle enough to avoid triggering a\
hen phalanx of\
social diplomacy.\
But the asshole deflected her thrusts\
without breaking a sweat. In\
\
the smarts department,  he was\
outclassed,  but in the attitude\
department he had\
her number.</\
p>\
<p>Why\
did I find this dynamic the\
\
most interesting? Background helps.\
She was dating a considerably older\
man who was\
not present at\
this event,  an alpha male\
in his own right,  for\
\
many years. Perhaps,  intimate\
familiarity with her own alpha braces\
her for the\
\
abyss that\
always looms ominously to eternally capture\
a woman&#8217;s\
heart\
should she become completely unguarded\
. She sees in the asshole\
boyfriend of her friend\
the power\
the alpha male has over all\
female sense and reason,  and\
she\
wants to put him on\
notice. It is her redemption\
.</p>\
<\
p>\
More interesting,  she alone among\
all the girl friends never consoled\
her\
smitten friend,  never attempted\
to introduce her to new men\
,  and never assuaged\
her ego\
by telling her she could do\
better. She was smart enough\
to\
know those kinds of interventions have no effect and,  worse,\
usually result in\
the opposite of\
what was intended. There&#\
8217;s an unwritten rule\
\
among very high-value women\
who date alpha males &#8212; the\
hate is for show. No woman would seriously give up the pleasure she gets\
from dating the alpha jerks she loves. They&#8217;d all poach\
each other&#8217;s boyfriends given half the chance,  and they know\
it.</p>\
'

gm = epub.EpubHtml(title='state of mind',
file_name='state_of_mind.xhtml',
lang='en')
gm.content='\
</h2>State Of Mind</h2>\
<p><em>\
i loved that he was so \
powerful i was nothing.<br \
/>\
</em>&#8211; \
O </p>\
<p\
>What is it that separates \
those select few men from all \
the rest? The ones who \
seemingly have no trouble getting pussy \
when they want and how they \
want it? The ones who \
wield illimitable power to inflame the \
desires of women?</p>\
\
<p>The key to \
their power is not money or \
sports cars or beach houses or \
post graduate degrees or 50 inch \
plasma TVs or chocolate covered strawberries \
on a bed of rose petals \
or any of that shit. \
All of that is incidental and \
is only important to the extent \
that it improves your state of \
mind. No,  the real \
source of this power is already \
within you. It is how \
you SEE YOURSELF. It is \
your decision to move through the \
world without apology,  to set \
aside complaining for decisive action,  \
to let your brass balls do \
your talking for you.</p\
>\
<p>The quintessential \
masculine quality women can&#8217\
;t resist is SUPREME UNSHAKEABLE \
CONFIDENCE. You can be poor\
,  out of shape,  stupid\
,  unemployed,  addicted to drugs\
,  and meet every one of \
society&#8217;s standards \
for LOSERNESS but if you radiate \
those confident vibes that say you \
are PERFECTLY FUCKING PLEASED WITH YOURSELF \
you will get laid ALL THE \
TIME. And the kinds of \
girls who get wet for such \
men aren&#8217;t \
just bar sluts. Smart women\
,  women with high self-\
esteems and MBAs and,  yes\
,  even &#8212; ESPECIALLY \
&#8212; HARDCORE FEMINISTS will \
crave the cock of the man \
who exudes such power and happily \
take it IN THE FACE and \
UP THE ASS if it means \
he will grace her with the \
pleasure of his company for a \
little while longer.</p>\
\
<p>THIS is the \
kind of power that matters. \
FUCK the normal rules. You \
make the rules now. They \
tell you to give give GIVE \
till it hurts,  to do \
your duty and throw yourself in \
the blood-soaked grinding gears \
of the KorporateAkademiaKredentialist Krell Machine in \
service to society&#8217;\
s great gaping maw and then \
maybe&#8230; MAYBE&#\
8230; one day you&#\
8217;ll be lucky enough \
to get chained for life to \
some mediocre pussy and infrequent,  \
tepid sex,  whereupon you will \
work yourself tirelessly to the bone \
shuffling your ungrateful brats through one \
societal sacramental rite of passage after \
another feeding the endless,  insatiable \
hunger of the machinery of the \
state. And they will pat \
you on the head for your \
devotion to the cause with lateral \
promotions and certificates of exemplary service \
and announcements in the wedding pages \
of the local paper and a \
brand new set of steak knives\
.</p>\
<p>\
FUCK</p>\
<p\
>THAT</p>\
<\
p>NOIZE.</p>\
\
<p>There&#8217\
;s a dirty little secret \
they don&#8217;t \
want you to know. And \
everyone is in cahoots,  from \
the alphas to the betas to \
the keepers of the vagina. \
It is this: You don\
&#8217;t need to play by their rules to get \
what you want! Women will \
still FLOCK to you if you \
shit all over everything you were \
taught you needed to do to \
earn their love as long as \
you do it with STYLE and \
UNWAVERING BOLDNESS and a TAKE IT \
OR LEAVE IT attitude. Because \
the simple truth is that the \
right attitude counts for more than \
all the material possessions in the \
world.</p>\
<p\
>The POWER is in your \
head.</p>\
'


gm2 = epub.EpubHtml(title='the naturals dilemma',
file_name='the_naturals_dilemma.xhtml',
lang='en')
gm2.content='\
<h2>The Natural''s Dilemma</h2>\
<p>The Natural &#8212; the man who has \
a seemingly otherworldly ability to entrance \
women. The Natural &#8212\
; not the CEO,  nor \
the jet fighter,  nor the \
doctor &#8212; is the \
man most men secretly admire and \
wish they had some of his \
mysterious mojo.</p>\
<\
p>But in reality he \
does not possess any magical abilities \
out of reach of ordinary men\
. The Natural is similar to \
the self-taught pickup artist\
,  with the critical distinction being \
that the former assimilated the lessons \
of love earlier in life. \
His masterstrokes paint the canvas of \
women effortlessly because he has been \
in training since he first noticed \
that girls and boys are different\
. If you break down the \
game of Naturals,  you&#\
8217;ll learn that their \
maneuvers and tactics and strategies,  \
far from being indefinable essences that \
only a very few lucky can \
lay claim to,  are in \
fact identical to the blueprints of \
learned game.</p>\
<\
p>Neither is the Natural \
necessarily good-looking. Many \
Naturals,  perhaps most of them\
,  are nondescript in the looks \
department. But because there is \
good reason to think a lot \
of them have inherited the Dark \
Triad suite of personality traits,  \
they are skilled at <a \
href="https://heartiste.\
wordpress.com/2012/\
12/05/evidence-\
that-peacocking-works/" \
target="_blank">presenting themselves \
in a way</a> \
that projects their sex appeal,  \
or invents it whole cloth,  \
if need be.</p>\
\
<p>No,  what \
the Natural has that mere mortals \
don&#8217;t is \
this: UNSTOPPABLE CONFIDENCE. They \
had the <a href="\
https://heartiste.wordpress.\
com/2012/03/\
08/the-aloof-\
alpha-attitude-explained/" \
target="_blank">ALPHA ATTITUDE\
</a> at a young \
enough age that it became ingrained \
to such an extent they rarely \
yield to the temptation to doubt \
their appeal to women.</p\
>\
<p>But the \
Externally Validated Natural who has spent \
a lifetime leaning on his looks\
/social connections/fame to \
get laid has a dilemma. \
As a reader puts it:</\
p>\
<blockquote><p\
>I&#8217;ve \
said it many times before,  \
the most pathetic thing in the \
world is a natural who has \
<a href="http://\
www.rooshv.com/\
you-have-no-\
idea-how-easy-\
it-is-for-\
good-looking-men#\
comment-66324" target="\
_blank">lost his mojo</\
a>.</p></blockquote>\
\
<p>The very blessing \
that makes The Natural an early \
adopter ladykiller is the curse that \
hobbles him later in life when \
challenges arise that introduce cracks to \
his impenetrable edifice of entitlement. \
You see,  the Externally Validated \
Natural has not bothered to learn \
the crimson arts. He has \
not mastered the state control that \
is necessary when inevitable dry spells \
occur,  or when glances from \
women are fewer and farther between\
,  or when uppity women with \
visions of mcmansion upgrades dancing in \
their heads give him shit he \
is not accustomed to receiving. \
He has never studied how to \
remain aloof and indifferent in the \
face of female fickleness because he \
has rarely experienced what life is \
like as a beta male who \
must battle to be loved,  \
rather than watching love fall in \
his lap like autumn leaves.</\
p>\
<p>The \
Natural who understands on a more \
than superficial level the nature of \
women,  and who has a \
working familiarity with game concepts,\
is a force ten charmer.\
Most Naturals don&#8217;\
t; they do the right\
things without knowing how or why\
they do them. When success\
eludes them and the expected warmth\
from women is missing,  they\
are left with nothing,  no\
storehouse of knowledge or pride of\
past successes achieved through self-\
aware hard work,  to pull\
them up from a dangerous downward\
spiral into the betatude they never quite understood either.</p>
'


gm3 = epub.EpubHtml(title='the underrated alpha male quality',
file_name='the_underrated_alpha_male_quality.xhtml',
lang='en')
gm3.content='\
<h2>The Underrated Alpha \
Male Quality</h2>\
<\
p>At a social gathering \
with friends and lovers,  I \
witnessed an attempted pickup unfold between \
an alpha male and a cute \
girl. We were a merged \
group of three girls and two \
men,  including myself,  and \
everyone there was known to me \
in more than a passing fashion\
. (I use the term \
   &#8220;alpha male\
   &#8221; as shorthand \
   to describe the constellation of \
   personality traits he possessed which \
   gave him an advantage in \
   the mating market. He \
   is not a particularly good\
   -looking man,  but \
   I suspect most girls would \
   say he is at least \
   not hard on the eyes\
   .)</p>\
<p\
>The girls with me knew \
that said alpha male was single \
and looking,  (ladies,  \
               we&#8217;re \
               ALWAYS looking),  and pow\
-wowed with each other to \
find a third girl they knew \
to be single as well for \
a possible alpha male-cute \
girl love copulation. Apparently,  \
not only do girls want alpha \
males for themselves,  they also \
want them for their friends. \
It&#8217;s that \
primeval female harem-managing mentality \
rising to the fore.</p\
>\
<p>One of \
the girls briefly absconded to another \
room and returned with a girl \
friend in tow who she wished \
to introduce to the alpha male\
. (I love using these \
   terms because I know how \
   much it chafes the asses \
   of the right sorts of \
   people.) The third girl \
was in transit to another subgroup\
,  and her slightly puzzled look \
suggested that she did not know \
why she was being pulled over\
. After a round of hellos\
,  I watched and listened,  \
from as sly a vantage point \
as I could muster under the \
circumstances,  the conversation that ensued \
between the alpha male and the \
cute girl summoned to unwittingly participate \
in his machinations.</p>\
\
<p>She looked him \
over as he began speaking,  \
and I could tell there lacked \
any sort of insta-spark \
of delight at his physical countenance\
. Nevertheless,  a man does \
not become an alpha male by \
abandoning all women who don&#\
8217;t instantly take a \
shine to his looks. For \
the first minute or two,  \
she would periodically glance at the \
girl friend to my side with \
that &#8220;why don\
&#8217;t you join \
in on this conversation so that \
I can impatiently slip away like \
a thief in the night&#\
8221; eye squeeze that women \
are so naturally adept at executing\
.</p>\
<p>\
But then a funny thing happened \
on the way to a certain\
,  subtle SWPL rejection where all \
feelings are spared in the most \
sadistic manner possible: the vibe \
turned in his favor. I \
can&#8217;t tell \
you the exact moment of redemption\
,  but I can say that \
the energy between them got a \
boost in the second or two \
after he dropped what can only \
be charitably described as a couched \
insult.</p>\
<p\
>&#8220;Well at least \
you&#8217;re still \
in your heels. Most girls \
like you are trading in for \
flats at this hour.&#8221\
;</p>\
<p>\
Her head snapped back. She \
was at full attention. Gone \
was the exasperated sideways glance for \
a rescuer,  replaced by flushed \
indignation that is the telltale mark \
of blood pipelined directly between the \
hamster and the vagina. A \
few hollow protests to the contrary \
notwithstanding,  she fell quickly into \
his orbit and they were off \
to the races. He had \
pricked her safe and secure but \
ultimately flimsy bitch bubble,  and \
she could not be happier for \
it.</p>\
<p\
>Now some of you readers \
are sure to lay the credit \
for his success on that convo\
-refueling neg which slices and \
dices bland boring expectations like a \
ginsu. You&#8217;\
d only be partly right in \
your assumptions. You see,  \
the neg was really just a \
culmination of something else,  some \
other ineffable quality,  that alpha \
males have in mass quantities: \
    persistence.</p>\
<\
p>Not that cringing,  \
awkward,  pushy,  socially uncalibrated \
persistence that a few oddly aggressive \
beta and omega males employ,  \
but the calm,  controlled,  \
almost serene persistence that doesn&#\
8217;t spook girls and \
which signals a strong,  dominant \
masculinity that women crave. It \
might be more precise to call \
it &#8220;steadiness&#\
8221; rather than persistence.</\
p>\
<p>The \
alpha male at this function knew \
she wasn&#8217;t \
immediately into him. The way \
he handled this &#8220;\
setback&#8221; wasn&#\
8217;t to slink away \
like a defeated herb,  or \
pump up the volume in a \
desperate last gasp maneuver to capture \
her attention. He wasn&#\
8217;t implicitly apologetic for \
the convo lull (as if \
                it was his responsibility to \
                keep everyone entertained),  nor \
was he giving any outward sign \
that he felt any pressure to \
perform.</p>\
<p\
>He simply stayed rooted at \
his spot,  never wavered in \
his eye contact,  maintained a \
neutral vocal cadence,  and never \
stupidly smiled to occupy dead air \
as so many less confident men \
are wont to do. He \
just kept&#8230; listening\
. And talking. And raising \
a single eyebrow. And leading \
the topic of discussion. And \
refraining from showing any discomfort with \
her feints to escape his company\
.</p>\
<p>\
And that was how he won \
her. Slow and steady and \
persistent and unshakeable. His body \
language and unperturbed social grace was \
the foundation upon which she was \
able to lean for evidence of \
alpha maleness. The neg was \
only icing on his seductive cake\
. The best time to drop \
a neg is when it is \
least expected,  not when it \
is obviously a craven effort to \
&#8220;win over&#\
8221; an intransigent girl. \
For him,  the neg was \
an adjunct that complimented his entire \
game repertoire.</p>\
<\
p>The alpha male is \
both aloof and persistent. His \
aloofness is more a vague impression \
that flows from his attitude,  \
and his persistence is a dagger \
that sneaks up on women and \
chips away at their coyness. \
When you can finally grasp that \
seeming contradiction and apply it in \
real social interactions,  your game will have matured immeasurably.</p>\
<p>Never listen to \
man-haters aka feminists who \
claim that women don&#8217\
;t like persistent men. \
They do. Women love persistent \
men who are persistent from a \
position of want,  not need\
. Women don&#8217;\
t love the idea of persistence \
because they associate it,  perhaps \
justifiably,  with overly aggressive meatheads \
throwing themselves at random vaginas during \
garbage hour. But now you \
know that there is better way \
to be persistent. And that \
you are doing honor to your \
alpha male ancestors by pursuing that \
scared little bunny to the farthest \
corners of the warren,  instead \
of turning tail the first time \
the bunny hops away a few \
feet from your swiping paws.</\
p>\
'

gm4 = epub.EpubHtml(title='inner game',
file_name='inner_game.xhtml',
lang='en')
gm4.content='\
<h2>Inner Game</h2>\
<p>I have a\
friend who is very self-\
critical. When we go out\
to meet girls he will handicap\
his game by being too hard\
on himself. When he isn\
&#8217;t weaseling out\
of approaching girls with every excuse\
in the book he is projecting\
an overly attentive vibe when he\
does manage to enter a set\
. In the field,  I\
&#8217;d often hear\
him say:</p>\
<\
p>&#8220;I wonder\
if she got my jokes?&#\
8221;</p>\
<p\
>&#8220;I hope I\
didn&#8217;t come\
off as too needy.&#8221\
;</p>\
<p>&#\
8220;She&#8217;\
s probably looking for a different\
type of guy.&#8221;</\
p>\
<p>Poor\
inner game &#8212; what\
is known by other jargon as\
your state of mind or your\
self confidence &#8212; is\
inwardly directed. Good inner game\
is outwardly directed. It&#\
8217;s the difference between\
berating yourself for not winning over\
others and berating others for not\
winning over you. The men\
who are naturally good with women\
live outside their minds &#8212\
; they are externally focused.\
The downside is that they are\
usually not very introspective,  but\
who cares about that shit when\
you&#8217;re getting\
pussy? Introspection is for dainty\
young women in sundresses picking buttercups\
in meadows.</p>\
<\
p>If my friend had\
good inner game what he would\
have said is:</p>\
\
<p>&#8220;She\
loses points for not having a\
good sense of humor.&#8221\
;</p>\
<p>&#\
8220;She&#8217;\
s the kind of girl who\
hides her insecurity behind aloofness.&#\
8221;</p>\
<p\
>&#8220;I&#8217\
;ll chat with her to\
see if she&#8217;\
s the type of girl I\
want in my life.&#8221\
;</p>\
<p>\
I hear a lot of talk\
about how Game routines are going\
stale,  and chicks see right\
through them. In fact,\
the problem isn&#8217;\
t typically with the routines,\
it&#8217;s with\
the confidence and congruence in which\
they are delivered. If your\
inner game isn&#8217;\
t solid then what you present\
to the outside world won&#\
8217;t match what you\
are feeling inside. Your inner\
game is reflected through your body\
language and voice tone,  so\
however clever your routines they will\
strike a false note if you\
don&#8217;t internalize\
the confidence you are trying to\
portray. You will betray yourself\
with negative thinking.</p>\
\
<p>Fake it till\
you make it means faking that\
internal confidence as well as the\
external behavior. This is not\
as hard as it sounds.\
Every time you feel self-\
doubt and talk yourself into inaction\
,  yell &#8220;Stop\
!&#8221; out loud,\
and your brain will reboot.\
You then consciously reframe your thought\
processes to put the burden of\
approval seeking on those around you\
. With good inner game you\
can say just about any ridiculous\
routine and the girl will be intrigued.</p>\
<p>The most important change in thinking you can make:</p>\
<p><strong>You\
are not there to win over\
women,  they are there to\
win over you.</strong></\
p>\
<p>Keep\
saying this over and over until\
you begin to believe it.\
You are re-wiring yourself\
. Don&#8217;t\
worry about the truth or falsity\
of it. That&#8217;s irrelevant.</p>\
<p>The beauty of\
this system is that it turns\
the seduction template on its head\
. Co-opting a woman\
&#8217;s natural choosiness\
and making yourself the chooser instead\
of the chosen is extremely attractive\
to women. Because it hardly\
ever happens this way,  women\
will happily strive to win the\
approval of a man who is\
clear in his words and his\
actions that he is judging them\
for worthiness of his attention,  and not the other way around.</p>\
'


gm5 = epub.EpubHtml(title='are ugly women necessary as stepping stones',
file_name='are_ugly_women_necesasry_as_stepping_stones.xhtml',
lang='en')
gm5.content='\
<h2>Are Ugly Women Necessary As Stepping Stones?</h2>\
<p><em>Alert: Intrapickup squabble!</em></p>\
<p>Is it true\
that an aspiring womanizer &#8212\
; or even a typical man\
in a billowy button-down\
who wants to improve his love\
life &#8212; must pay\
his dues with ugly women before\
he can achieve the goal of\
banging hotter women? The question\
hints at a significant fault line\
in current pickup thinking,  precisely\
because it throws into stark relief\
the ego-shattering human impulse\
to judge men <a href\
="https://heartiste.wordpress\
.com/2008/10\
/21/misconceptions-about\
-the-alpha-male\
/" target="_blank">based\
on the quality of women they\
pull</a>.</p>\
\
<p>I&#8217\
;ll paraphrase a reader&#\
8217;s objections,  who\
asked not to be directly quoted\
:</p>\
<p><\
em><a href="http\
://www.rooshv.com\
/the-i-have\
-standards-excuse" target\
="_blank">Roosh&#8217\
;s idea</a>\
that you have to bang a\
lot of unattractive women to get\
hotter women is not persuasive.\
What helps is getting laid regularly\
,  which doesn&#8217;\
t necessarily require cutting your teeth\
on ugly chicks. You only\
need one woman to get laid\
regularly,  so such a strategy\
obviates the need to fill up\
your notch post with lots of\
uglies and plain janes. Ideally\
,  your &#8220;regular\
lay&#8221; should be\
in the 6 to 8 range\
,  but if you&#8217\
;re a newbie you may\
have to start with 4s and\
5s. Picking up large numbers\
of less attractive women may give\
you experience with logistics and help\
with honing your routines,  but\
that is the relatively easy part\
of game. Getting laid regularly\
,  even if it&#8217\
;s with one woman,\
is all a man needs to\
step up to the next higher\
beauty class.</em></p\
>\
<p>My opinion\
on this matter falls somewhere between\
Roosh&#8217;s and\
the anonymous reader&#8217;\
s takes. Roosh is entirely\
correct to note that men who\
use the &#8220;I\
have standards&#8221; excuse\
are,  more often than not\
,  men who aren&#8217\
;t living up to their\
professed high standards. It&#\
8217;s similar in spirit\
to the internet nerd sour grapes\
syndrome,  in which hot chicks\
that are unavailable to them are\
deemed unworthy of their loving nerd\
attention because of some ridiculously trivial\
flaw,  like pointy elbows.</\
p>\
<p>Roosh\
is also onto something when he\
advocates for having flexible standards.\
If 8s and above are all\
you will deign to approach,\
then there are going to be\
times and places when and where\
you will endure some long,\
tough dry spells,  and this\
is especially true if you are\
an average guy with average game\
and above average horniness. Unless\
you have rock solid inner game\
and unshakeable confidence that enables you\
to weather extended down times without\
losing your pickup magic or your\
aura of charismatic fuckability,  those\
dry spells will hurt your interactions\
with women. Like dogs can\
smell fear,  women can smell\
celibacy.</p>\
<p>The reader suggests\
that the ideal route for men\
to take to avoid sexless purgatory\
while keeping the ladder-climbing\
option open is to gun for\
the decent-looking regular lay\
. This allows a man to\
avoid the dispiritment that accompanies fucking\
too many uglies while also sparing\
him the stink of celibacy that\
erodes confidence and spooks hot chicks\
.</p>\
<p>\
And that&#8217;s\
where I part company with Roosh\
and favor the life strategy of\
the anonymous reader. Fucking uglies\
,  in even small quantities and\
in temporary bouts,  risks flirting\
with depression and slumping into a\
long-term rut. I\
don&#8217;t come\
by this view speculatively. I\
have some real world trials by\
trolls from which to evangelize.\
I&#8217;ll give\
you an example I&#8217\
;m thinking of from years\
ago:</p>\
<p\
>I had spent a few\
weeks fucking a 5. It\
was only four bang sessions,\
but that was enough to alter\
my self-perception and mood\
. I had gone through a\
bad breakup and she (the\
                     5) presented herself,\
fortuitously,  almost immediately after the\
final severance from my ex.\
She was friendly and sweet,\
and open to meeting someone.\
I gamed her but hardly needed\
more than my first wave artillery\
; she melted quickly. She\
had a good body,  so\
despite her plain face the sex\
was good. But I couldn\
&#8217;t help notice\
it was not as good as\
<a href="https://\
heartiste.wordpress.com/\
2007/08/30/\
hotter-women-better-\
sex/" target="_blank">\
sex with hotter women</a\
>.</p>\
<p>\
Just at the point I was\
getting the full measure of my\
single man&#8217;s\
confidence back,  the 5 conveniently\
left town,  rescuing me from\
the awkwardness of a messy dumping\
I knew had to be done\
. However,  upon leaving,\
the sexless rut began to reappear\
. Two weeks went by with\
no acceptable nibbles on my penile\
line. A buddy who was\
a wingman at the time suggested\
I meet up with a girl\
he had failed with himself as\
a sort of friendship offering in\
difficult times.</p>\
<\
p>&#8220;You&#\
8217;ll really like this\
girl. She&#8217;\
s totally your type. A\
solid 8. Very hot,\
blonde.&#8221;</p>\
\
<p>&#8220;Oh\
yeah? If she&#8217\
;s so hot,  why aren&#8217;t you working on her?&#8221;</p>\
<p>&#8220;I\
did. I got nowhere,\
but it&#8217;s\
OK,  I prefer brunettes.\
We hang out together. She\
makes me look good when we\
go out.&#8221;</p\
>\
<p>&#8220;\
So you want me to meet\
her? Hmm.&#8221;</\
p>\
<p>&#8220\
;Yes,  you&#8217\
;ll thank me.&#8221\
;</p>\
<p>\
We met,  all four of\
us &#8212; me,\
the &#8220;hot blonde\
8&#8221;,  my friend\
,  and his current girlfriend &#\
8212; late at night under\
cover of a dark lounge.\
I didn&#8217;t\
know where my friend&#8217\
;s head was,  but\
she was no 8. Yes\
,  she had blonde hair,\
but that was about where the\
confirmation of my friend&#8217\
;s powers of observation ended\
. From what I could glean\
through the dim club light and\
my alcoholic haze,  she was\
no better than a 6,\
and maybe even a 5.</\
p>\
<p>Nevertheless\
,  I was horny,  and\
feeling down. I could use\
the pickmeup pickherup. We trundled\
outside,  into a cab,\
and I took her back to\
my pad. Inside my place\
,  lights at full blast,\
I was sorely disappointed to realize\
my friend&#8217;s\
&#8220;solid 8&#\
8221; was a weak 4\
. I had never fucked a\
4 before,  and never would\
again.</p>\
<p\
>Too late to reverse course\
,  and bored into conspiracy,\
I lamely escorted her into my\
bed,  and quickly swung her\
into the doggy-style position\
where exposure to her face would\
be limited. Her body wasn\
&#8217;t half-\
bad,  but not good enough\
to compensate; my dick went\
limp inside her vagina. I\
imagine that has to be a\
girl&#8217;s worst\
nightmare; up front rejection in\
the form of a backturn or\
a wandering eye is bad enough\
,  but getting rejected in the\
most softeningly obvious way possible when\
you are literally giving it everything\
you&#8217;ve got\
,  your womanhood deeply committed&#\
8230; well,  that&#8217;s gotta sting.</p>\
<p>I couldn&#\
8217;t be bothered to\
make excuses. She dressed and\
left in silence. My blue\
mood hardened. I cursed my\
friend&#8217;s taste\
in women. I took a\
shower to wash off the dirt\
that had alighted upon my soul\
.</p>\
<p>\
Two women,  one borderline ugly\
and the other plain as unsyruped\
pancakes,  in a row and\
I was done with the idea\
of it. Their company,\
however genial and accommodating,  did\
nothing to lift my spirits or\
gird my confidence. Just the\
opposite,  in fact: I\
fell deeper into self-flagellation\
.</p>\
<p>\
One week after the limp-\
out incident,  I hit up\
a local lounge and met an\
8.5 whom I would\
spend the next five months fucking\
in gloriously hedonistic abandon. I\
have yet to share my bed\
since then with a woman lower\
than a 6.5.\
I learned my lesson.</p\
>\
<p>I&#\
8217;m as horny a\
guy as you&#8217;\
ll find,  but I have\
to admit not so horny that\
I&#8217;ll start\
rummaging through the 3 and 4\
kitchen trash if there&#8217\
;s no four star restaurant\
available. Maybe that&#8217\
;s a problem of getting\
laid too regularly &#8212;\
you lose that wall-climbing\
horniness that would compel you to\
stick it in the most convenient\
wet hole. Ugly girls as\
stepping stones to hotter women sounds\
good in theory,  but in\
reality sex with them too often\
&#8212; and too often\
can happen a lot faster than\
most men realize &#8212;\
is not only a time and\
energy suck,  but a depressive\
drug that corrodes self-confidence\
.</p>\
<p>\
Perhaps this feeling &#8212;\
this sex dynamic &#8212;\
varies by race,  age and\
baseline dignity. If so,\
more power to the guys who\
don&#8217;t mind\
dumping fucks in seacows and butterfaces\
. I can&#8217;\
t bring myself to do it\
,  even if it&#8217\
;s all the local talent\
has to offer. My minimum\
threshold in women&#8217;\
s looks is 6,  under\
which it becomes almost physiologically impossible\
for me to complete the bang\
.</p>\
<p>\
My inner game is strong enough\
now that I can afford to\
risk a month or two downtime\
without getting too rusty or too\
doubtful of my skills. I\
would only use an ugly girl\
who fell below my minimum looks\
threshold as a stepping stone in\
the most dire of circumstances,\
such as if my dry spell\
extends beyond two months,  or\
I&#8217;ve taken\
to,  ahem,  &#8220\
;mood enhancers&#8221;\
that give me 24 hour wood\
.</p>\
<p>\
So you might say that the\
reader&#8217;s strategy\
is the way to go if\
you are a high risk for\
lengthy dry spells,  and your\
game and self-possession aren\
&#8217;t strong enough\
to carry you through a slump\
slumming it with ugly chicks.\
Alternatively,  Roosh&#8217;\
s strategy &#8212; to\
skip the &#8220;regular\
lay&#8221; girlfriends and\
just focus on getting laid even\
if the talent available is not\
up to snuff &#8212;\
is better if you can&#\
8217;t tolerate any kind\
of dry spell,  if your\
dick is indiscriminate,  and if\
your game is good enough that\
regular pickup with little downtime is\
within the realm of possibility.</\
p>\
<p>TL\
;DR Don&#8217;\
t make a habit of banging\
ugly chicks. It can be\
as bad for your self-\
confidence as involuntary celibacy.</p\
>\
'

gm6 = epub.EpubHtml(title='i only play games with girls who deserve it',
file_name='i_only_play_games_with_girls_who_deserve_it.xhtml',
lang='en')
gm6.content='\
<h2>I Only Play Games With Girls Who Deserve It</h2>\
<p><a href="\
https://heartiste.files.\
wordpress.com/2008/\
06/hott.jpg"></\
a>I get this occasionally\
from some girls I date,\
usually after they have dumped a\
major shit test on me and\
I am forced to respond with\
advanced game:</p>\
<\
p><em>&#8220;\
Why does everything have to be\
a test with you?&#8221\
;</em></p>\
<\
p>I thought about this\
and reflected on my history with\
women. It was partly true\
. With certain girls I&#\
8217;ve dated,  I\
was in game mode <a\
href="https://heartiste.\
wordpress.com/2007/\
04/11/excerpt-\
from-the-book-\
of-alpha/" target="\
_self">all the time</\
a>. One girl even said\
that she knew when I would\
return her calls because I would\
always wait the requisite 20 minutes\
.</p>\
<p>\
Dispiritingly,  dogmatic game &#8212\
; press this button,  pull\
that lever &#8212; will\
work as intended. You can\
<img data-attachment-\
id="665" data-\
permalink="https://heartiste.\
wordpress.com/2008/\
06/19/i-\
only-play-games-\
with-girls-who-\
deserve-it/hott/"\
data-orig-file="\
https://heartiste.files.\
wordpress.com/2008/\
06/hott.jpg"\
data-orig-size="\
450, 323" data-\
comments-opened="1"\
data-image-meta="{&\
quot;aperture&quot;:&\
quot;0&quot;,\
&quot;credit&quot\
;:&quot;&quot;, &\
quot;camera&quot;:&\
quot;&quot;, &quot\
;caption&quot;:&quot\
;&quot;, &quot;\
created_timestamp&quot;:&quot;\
0&quot;, &quot\
;copyright&quot;:&quot\
;&quot;, &quot;\
focal_length&quot;:&quot;\
0&quot;, &quot\
;iso&quot;:&quot\
;0&quot;, &\
quot;shutter_speed&quot;:&\
quot;0&quot;,\
&quot;title&quot\
;:&quot;&quot;}" data\
-image-title="hott\
" data-image-description\
="&lt;p&gt\
;hott&lt;/p\
&gt;\
" data-\
medium-file="https://\
heartiste.files.wordpress.\
com/2008/06/\
hott.jpg?w=\
300&#038;h=\
209" data-large-\
file="https://heartiste.\
files.wordpress.com/\
2008/06/hott.\
jpg?w=450"\
class="alignright size-medium\
wp-image-665"\
src="https://heartiste.\
files.wordpress.com/\
2008/06/hott.\
jpg?w=300&#\
038;h=209"\
alt="hott"   />never\
truly BE YOURSELF with women because\
almost all men being themselves will\
regress to lounging on the couch\
in their underwear as long as\
their basic needs are met.\
Literally,  you could put a\
feeding tube in a guy&#\
8217;s mouth,  a\
drainage tube up his anus,\
a playstation controller in his hand\
,  and a girl&#8217\
;s mouth on his cock\
and he&#8217;ll\
lay there like that until he\
spontaneously self-combusts.<a\
href="https://heartiste.\
files.wordpress.com/\
2008/06/hott.\
jpg"></a></p>\
\
<p>And women too\
. Look what happens to women\
who have totally given up on\
finding a man &#8212;\
they blow up like whales,\
wear flip flops all the time\
,  and cut their hair short\
. When you see a frumpy\
,  charmless,  fat woman you\
know she is BEING HERSELF.</\
p>\
<p>So\
why do I overgame with some\
girls and not others? It\
&#8217;s not a\
looks thing. Some of the\
prettiest girls I&#8217;\
ve been with were a breeze\
to handle once in a relationship\
,  even though during the first\
crucial dates they were the toughest\
to game. Hot girls tend\
to frontload their gameplaying,  so\
if you breach their beachhead it\
&#8217;s a clear\
march to center city.</p\
>\
<p>I think\
it&#8217;s an\
ego issue,  or maybe one\
of intelligence. Very smart girls\
are always on the lookout for\
Machiavellian maneuvers in their men because\
they do it themselves. The\
world is our mirror. Combined\
with a powerful but sensitive ego\
,  a girl like this will\
be hyperaware of manipulation and deathly\
afraid of getting hurt. <\
a href="https://heartiste\
.wordpress.com/2008\
/05/11/circles\
/" target="_self">Stephane\
of Ideagasms</a> calls\
these types of women (and\
                      men) Interrogators &#8212\
; a subspecies of Energy Vampires\
:</p>\
<blockquote><\
p>Interrogators are (initially\
                     ) difficult to detect,\
because<br />\
they are\
perfectionists; These people see the\
life as a<br />\
\
competitive GAME and they are quite\
masterful when it comes<br\
/>\
to manipulating others.  </\
p>\
<p>Their\
philosophy?  &#8220;Life\
is just a game &#8211\
; You either play<br\
/>\
by the rules,  or\
you&#8217;re a\
loser.&#8221; They see\
the world as<br />\
\
Win/Lose instead of Win\
/Win.</p>\
<\
p>That&#8217;\
s a great metaphor for explaining\
what Interrogators<br />\
do\
to people,  because when you\
spot an Interrogator and try<\
br />\
to gently point out\
what he or she is doing\
,  they too will<br\
/>\
pretend that they are innocent\
and that this heavily<br\
/>\
ingrained and entirely OBVIOUS pattern\
of behavior does not<br\
/>\
exist.</p>\
<\
p>Then they will turn\
around and casually remark that there\
is<br />\
something wrong\
with YOU. They&#8217\
;ll go,  &#8220\
;Why would you say<\
br />\
that? Why are\
you so PARANOID,  huh?&#\
8221; (Notice they are\
       not<br />\
really\
       asking a question,  but rather,  making a statement<br />\
about you.)</p>\
<p>Or they will\
accuse you of being &#8220\
;too sensitive&#8221;&#\
8230; as if<br\
/>\
*sensitivity* was a\
bad thing!</p>\
<\
p>MANY of the top\
&#8220;seduction community gurus\
&#8221; are simply<\
br />\
INTERROGATORS. This is\
why they &#8220;play\
the game&#8221; and\
have<br />\
all sorts\
of complicated &#8220;chess\
moves&#8221; and strategies\
for<br />\
interacting with\
women. They have a HIDDEN\
AGENDA.</p>\
<p\
>Interrogators ask a lot of\
rhetorical questions,  and often play\
<br />\
&#8220;\
Devil&#8217;s advocate\
&#8221;. But,  the\
questions they ask are not<\
br />\
questions at all!\
It is their attempt to break\
down your<br />\
reality\
in the form of negative presuppositions\
about you.</p></blockquote\
>\
<p>Overgaming can\
be caustic to forming a relationship\
with a girl you really like\
. The best relationships are built\
on a foundation of sincerity,\
not mutually asssured deconstruction. It\
&#8217;s a tragedy\
when the couple really like each\
other and the mutual gaming undermines\
the potential for a deeper connection\
. Game and ego-protection\
will always be a necessary component\
of any interaction you have with\
quality women,  but it should\
be relegated to a supplement after\
a certain amount of bonding has\
occurred. At some point,\
you have to open your heart\
and let the chips fall where\
they may.</p>\
<\
p>So when I game\
too much for too long,\
it&#8217;s with\
the girls who deserve it.\
If I&#8217;m\
getting shit tested all the time\
,  or she&#8217;\
s in <strong><a\
href="https://heartiste.\
wordpress.com/2007/\
04/25/dont-\
be-that-girl/"\
target="_self">Aloof and\
Indifferent</a></strong>\
mode every other day,  or\
I sense that she&#8217\
;s hiding something,  I\
will respond in kind. We\
calibrate our actions and behavior to\
match the other person&#8217\
;s. Women,  being\
the gatekeepers and mate choosers,\
are responsible for how men strategize\
to get in their pants and\
their hearts. If a girl\
makes it hard for a guy\
to be sincere by playing Miss\
Scheming Queen,  he will react\
with more game. If she\
&#8217;s letting him\
know how much she loves him\
,  he will be real with\
her.</p>\
<p\
>You get what you give\
.</p>\
<p>\
Make no mistake,  this is\
not an anti-game screed\
. Game is absolutely essential in\
the beginning stages (See:\
                      Mystery Method&#8217;\
                      s A1 &#8211;\
                      S3) for every women\
you want to sex,  unless\
your value is so much higher\
than hers that you can do\
nothing and she&#8217;\
ll throw herself on your junk\
. Relationship game is also important\
to keep the embers burning.</\
p>\
<p>But\
in time the doubt has to\
ease and the soul has to\
breathe. Anything less would be&#8230; uncivilized.</p>\
'


gm7 = epub.EpubHtml(title='builds charaacter to reject women',
file_name='it_builds_character_to_reject_women.xhtml',
lang='en')
gm7.content='\
<h2>It Builds Character To Reject Women</h2>\
<p>If you are a man who has never rejected \
a woman for sex or dating\
,  you are doing something wrong\
. You are,  in fact\
,  depriving yourself of one of \
life&#8217;s greatest \
pleasures and privileges,  and avoiding \
a true test of your masculine \
mettle.</p>\
<p\
>As we all know by \
now from the science,  from \
common sense,  and from reading \
my powerful words of genius,  \
the default barter mechanism in the \
sexual market is female choice,  \
male display. This is a \
natural consequence of the disparity between \
the scarcity of eggs and the \
surplus of sperm. But men \
are not entirely helpless to actively \
influence market prices; they choose \
as well. If men did \
not choose at all,  women \
would not have evolved an instinct \
for improving their looks through fashion\
,  makeup,  and exercise. \
If I had to put a \
number on it,  I&#\
8217;d say on average \
women do 70% of the \
choosing and men do 30% \
of the choosing. At the \
tails,  the alpha-iest \
men do all the choosing and \
have to beat off their female \
suitors while the fattest,  ugliest \
women must settle for whatever man \
will take them. The general \
trend,  though,  is upward \
dating for most women and a \
few men.</p>\
<\
p>The fact of this \
mating dynamic explains why turning the \
tables and exercising male choice is \
such a powerful psychological game technique \
for seducing the minds of women\
. By behaving as if you \
are actively choosing women,  and \
even occasionally rejecting them,  you \
mimic the natural actions of the \
top 10% of men whose \
default mating strategy is choosing from \
an illimitable source of pussy and \
wielding the merciless power of sexual \
rejection.</p>\
<p\
><strong>Maxim #18\
: The two fundamental propositions upon \
which all game theory rests are \
male choosiness and female abundance. \
All alpha males have these two \
mindsets in common.</strong></\
p>\
<p><strong\
>Corollary to the above: \
    Male choosiness and female abundance \
    do not necessarily have to \
    be true for the strategy \
    of behaving as if they \
    are true to be effective \
    at seducing women.</strong\
    ></p>\
<p\
>Try to put yourself in \
women&#8217;s shoes\
. When you are on a \
date,  imagine you are a \
woman. Think like she would \
think. Feel like she would \
feel. Is this girl right \
for me? Are we compatible\
? What are her values? \
I&#8217;m just \
not sure if she&#8217\
;s the one; let\
&#8217;s see what \
else she has going for her\
. I need to keep my \
options open. I&#8217\
;m not ready to make \
a decision. I really need \
to be wowed,  I wonder \
if she can do that for \
me. She seems kind of \
nervous. Is she dull? \
Am I out of her league\
? Damn,  she just said \
something stupid. Maybe she&#\
8217;s not the one\
.</p>\
<p>\
Keep thinking like this and soon \
your outward behavior will reflect your \
inward feelings. Suspend your disbeliefs \
long enough until they have become \
unshakeable beliefs. Once you have \
mastered the mindset of women,  \
you will have mastered women themselves\
.</p>\
<p><\
strong>Maxim #19: \
The alpha male thinks and acts \
more like a woman than a \
man in matters of seduction. \
He understands his adversary&#8217\
;s psychology,  and uses \
it to shatter her defenses.</\
strong></p>\
<p\
>The next time a woman \
who does not meet your attractiveness \
standards hits on you,  humor \
her for a bit,  lead \
her on,  then politely reject \
her.</p>\
<p\
>&#8220;What are you \
doing this Friday?&#8221;<\
br />\
&#8220;Oh\
,  I should tell you I\
&#8217;m seeing someone\
.&#8221;</p>\
<\
p>Do this even if \
you are hard up. Commanding \
the power of female/alpha \
male choosiness will enrich your soul \
and fortify your ego. You\
&#8217;ll feel bad \
for the girl for maybe 30 \
seconds,  but the value-\
boosting afterglow will last for weeks\
. This is all about long\
-term thinking. Capture the \
female essence of sexual choice and \
make it a part of you\
.</p>\
<p>\
Girls hitting on you is a \
rare event for most men,  \
so you&#8217;ll \
need to be more active in \
your policy of preferential sexual consumerism\
. As long as you are \
dating <a href="https\
://heartiste.wordpress.com\
/2007/11/14\
/dont-stop-thinking\
-about-the-next\
-girl/" target="_blank\
">two or more women simultaneously\
</a>,  you should have \
no qualms rejecting at least one \
of them for not being up \
to snuff. Choose one for \
dismissal and stop calling her for \
dates. It doesn&#8217\
;t have to be the \
least attractive chick; in fact\
,  it&#8217;s \
more character-building and alpha\
-boosting to reject an attractive \
girl for an odd facial tic \
or bland personality. If she \
doesn&#8217;t get \
the hint,  be candid and \
tell her she just isn&#\
8217;t right for you\
. Women,  especially 7s and \
up,  rarely hear this,  \
so it will tear at her \
soul like the claws and teeth \
of an army of demons. \
If you can withstand the brief \
flicker of guilt and loss of \
sexual opportunity,  her pain of \
rejection will actually feed your incipient \
alpha animal spirit,  stengthening you\
,  making you tougher,  more \
appropriately detached,  and able to \
clearly see and pursue your self\
-interest. Through the action \
of choosiness,  your self-\
worth will skyrocket. And others\
&#8217; evaluation of your \
worth will similarly follow.</p\
>\
<p>If you \
believe there are &#8220;\
better&#8221; or more \
&#8220;moral&#8221\
; paths to alphaness,  know \
this: Every alpha male is \
intimately familiar with the ego-\
stroking power of sexual choosiness. \
They have all,  good and \
bad,  enlightened and crass,  \
rejected women in one way or \
another and crushed their souls,  \
often on the <a href\
="https://heartiste.wordpress\
.com/2008/06\
/26/flimsy-excuses\
-i-use-to\
-get-girls-back\
-to-my-place\
/" target="_blank">flimsiest \
pretexts</a>. Some are \
kind enough to dress it up \
in polite fictions; others are \
id monsters who flaunt their sexual \
despotism without regard for social convention \
or righteous preening. But all \
have lowered the boom. It \
goes with the territory.</p\
>\
<p>The more \
women you reject,  the more \
women will sense your radiating power \
to inflict pain and loss and \
subsequently want you. Buttress your \
inner game by being choosy,  and rejecting freely.</p>
'



gm8 = epub.EpubHtml(title='how to inure yourself to beautiful women',
file_name='how_to_inure_yourself_to_beautiful_women.xhtml',
lang='en')
gm8.content='\
<h2>How To Inure Yourself To Beautiful Women<h2>\
<p>A thinking sort of reader writes:</p>\
<blockquote><p>The\
hedonistic treadmill concept says you&#\
8217;ll get reduced satisfaction\
from expanded consumption as you adjust\
to it. You won&#\
8217;t appreciate a Ferrari\
if you drive one everyday and\
the same applies to a steak\
dinner.</p>\
<p\
>When I&#8217;\
m on a winning streak with\
girls,  I feel they all\
get less hot. I find\
myself turning my head less often\
. I see pictures of girls\
that I thought were flawless and\
I see flaws. I find\
myself thinking about other areas of\
my life. Conversely,  when\
I&#8217;m not\
longer with a girl,  and\
I go into a slump,\
I find my ex was hotter\
than I remember.</p>\
\
<p>Girls can definitely\
tell when a guy is not\
impressed. I read football practice\
is often harder than the real\
game. I&#8217;\
m not sure we&#8217\
;ve invented a way to\
expose normal guys to beautiful women\
the same way that Tom Brady\
and Brad Pitt are exposed.\
Strippers,  porn,  movies,\
etc don&#8217;t\
work since they all work to\
raise the woman on the pedestal\
. <strong>[ed:\
           correct. there&#8217\
           ;s good exposure and\
           self-limiting exposure.\
           alpha males are exposed to\
           women&#8217;s\
           desire. johns and gawkers\
           are exposed to women&#\
           8217;s mercenary indifference\
           .]</strong></p>\
\
<p>I&#8217\
;m thinking a picture gallery\
of women as they age,\
or a picture gallery of models\
without makeup might be a good\
start.</p></blockquote>\
\
<p>Definitely something to\
this. While filet mignon will\
always taste better than ground chuck\
,  and a hot girl will\
always be a better lay than\
an ugly girl,  the pleasure\
that can be extracted from the\
tastier choices will,  with enough\
familiarity and dopamine receptor scorching,\
succumb to diminishing returns. (\
    Although it will never bottom\
    out as low as the\
    scant pleasure one receives from\
    cheap cuts of meat or\
    girls.)</p>\
<\
p>The blowback from dopamine\
-blasted beauty immunity is that\
all women,  even the ones\
you aren&#8217;t\
fucking,  start to seem less\
desirable,  or at least less\
worthy of sustained effort to earn\
their interest. And this is\
how ecologically self-perpetuating alpha\
males are made:</p>\
\
<p><strong>Maxim\
#12: The cumulative experience\
with hot women imbues the womanizer\
with a genuinely aloof aura that\
attracts even more women to him\
.</strong></p>\
<\
p><strong>Corollary to\
Maxim #12: If you\
don&#8217;t have\
an adequate amount of aloofness-\
inducing experience with hot women,\
act like you do.</strong\
></p>\
<p>\
Think about when you were,\
or how you are now,\
comfortably ensconced in a secure relationship\
with a girl. Objectively,\
she&#8217;s cute\
. When you first saw her\
,  your heart leapt upward in\
sync with your cock.</p\
>\
<p>But damn\
if you don&#8217;\
t espy<br />\
that\
as the days tick by<\
br />\
your wandering eye<\
br />\
roves wide as the\
sky.</p>\
<p\
>In graphical form,  this\
is known as the Beauty Power\
Law,  and it looks like\
this:</p>\
<p\
><img data-attachment-\
id="15435" data-\
permalink="https://heartiste.\
wordpress.com/2012/\
10/17/how-\
to-inure-yourself-\
to-beautiful-women/\
beautypowerlaw/" data-orig-\
file="https://heartiste.\
files.wordpress.com/\
2012/10/beautypowerlaw.\
png?w=500&#\
038;h=375"\
data-orig-size="\
800, 600" data-\
comments-opened="1"\
data-image-meta="{&\
quot;aperture&quot;:&\
quot;0&quot;,\
&quot;credit&quot\
;:&quot;&quot;, &\
quot;camera&quot;:&\
quot;&quot;, &quot\
;caption&quot;:&quot\
;&quot;, &quot;\
created_timestamp&quot;:&quot;\
0&quot;, &quot\
;copyright&quot;:&quot\
;&quot;, &quot;\
focal_length&quot;:&quot;\
0&quot;, &quot\
;iso&quot;:&quot\
;0&quot;, &\
quot;shutter_speed&quot;:&\
quot;0&quot;,\
&quot;title&quot\
;:&quot;&quot;}" data\
-image-title="beautypowerlaw\
" data-image-description\
="" data-medium-file\
="https://heartiste.files\
.wordpress.com/2012\
/10/beautypowerlaw.png\
?w=500&#038\
;h=375?w\
=300" data-large\
-file="https://heartiste\
.files.wordpress.com\
/2012/10/beautypowerlaw\
.png?w=500\
&#038;h=375\
?w=500" class\
="alignnone size-full wp\
-image-15435" title\
="beautypowerlaw" alt="" src\
="https://heartiste.files\
.wordpress.com/2012\
/10/beautypowerlaw.png\
?w=500&#038\
;h=375" height\
="375" width="500\
" srcset="https://heartiste\
.files.wordpress.com\
/2012/10/beautypowerlaw\
.png?w=500\
&amp;h=375\
500w,  https://heartiste.\
files.wordpress.com/\
2012/10/beautypowerlaw.\
png?w=150&\
amp;h=113 150w\
,  https://heartiste.files\
.wordpress.com/2012\
/10/beautypowerlaw.png\
?w=300&amp\
;h=225 300w,\
https://heartiste.files.\
wordpress.com/2012/\
10/beautypowerlaw.png?\
w=768&amp;\
h=576 768w,  https\
://heartiste.files.wordpress\
.com/2012/10\
/beautypowerlaw.png 800w"\
sizes="(max-width:\
    500px) 100vw,  500px\
    " /></p>\
<\
p>Beauty immunity is real\
,  and it affects every man\
\
,  relative to his beauty capture\
starting point. That is,\
a low value man will quickly\
tire of low value women if\
he manages long-term relationships\
(or long-term consecutive\
 hook-ups) with\
those low value women he fears\
he is fated to match.\
He will still want hot chicks\
,  but the additive experience with\
unattractive chicks will create in him\
an aloofness toward all unattractive chicks\
that is similar in psychological composition\
to the aloofness a high value\
man will feel for the hot\
chicks he routinely bangs and even\
the ones he hasn&#8217\
;t banged.</p>\
\
<p>THIS IS A\
GOOD THING. That aloofness is\
catnip to women. You may\
as well prop a neon sign\
over your head that says &#\
8220;Preselected by women who\
have come before you,  and\
who are standing right next to\
you.&#8221; Aloofness is\
one of those male characteristics that\
women are finely tuned to discover\
,  isolate,  and hone in\
on,  because it tells them\
,  subconsciously of course,  that\
THIS MAN,  this one right\
here,  has a lot of\
choice in women. ERGO,\
this man,  this one right\
here,  must be high value\
.</p>\
<p>\
I can attest to the tangible\
effects of the beauty immunity power\
law. When I&#8217\
;m in a solid relationship\
,  or when I&#8217\
;m on a hot streak\
dating multiple concurrent or consecutive women\
,  then all women in general\
start to feel more approachable,\
less insurmountable (heh),  and\
,  tragically,  less tolerable.\
The effect of familiarity with females\
and their foggy furrows is a\
steady glazing of my perception of\
their beauty,  until they seem\
as if their faces are an\
indistinguishable mass of downy cotton balls\
. Worse,  the tolerance,\
even enthusiasm,  I would have\
just talking and spending idle time\
with women yields more frequently and\
submissively to competing distractions,  like\
reading alone,  hanging with buds\
,  pursuing hobbies,  or elevating\
my status for a potential trading\
-up of lovers. Her\
charming little tics I loved during\
the first few months soon become\
swarms of buzzing annoyances,  and\
my mind begins the unstoppable drift\
to ELSEWHERE.</p>\
<\
p>THIS IS A BAD\
THING. That transcendental stirring rocketing\
up from the groin and ricocheting\
off the sternum when you first\
set your post-pubertal eyes\
on hot high school girls weakens\
in proportion to your success bedding\
them. The bloom on the\
rose wilts with too much fertilizer\
.</p>\
<p>\
But enough of that sentiment.\
The fact remains that inuring yourself\
to beautiful women,  and to\
beauty itself,  will make you\
a more lethal ladykiller.</p\
>\
<p>So how\
do you expose yourself,  as\
the reader suggested,  to beautiful\
women such that they hold less\
power over your faculties and their\
flaws are more evident to your\
senses?</p>\
<p\
>1. Bed a lot\
of them.</p>\
<\
p>Guaranteed to work,\
and that&#8217;s\
why it&#8217;s\
the most difficult solution to the\
beauty immunity puzzle.</p>\
<p>2. Train\
your mind away from pedestalization of\
female beauty.</p>\
<\
p>Remember <a href\
="https://heartiste.wordpress\
.com/the-sixteen\
-commandments-of-poon\
/" target="_blank">Poon\
Commandment</a> X?</\
p>\
<blockquote><p\
><strong>X. Ignore\
her beauty</strong></p\
>\
<p>The man\
who trains his mind to subdue\
the reward centers of his brain\
when reflecting upon a beautiful female\
face will magically transform his interactions\
with women. His apprehension and\
self-consciousness will melt away\
,  paving the path for more\
honest and self-possessed interactions\
with the objects of his desire\
. This is one reason why\
the greatest lotharios drown in more\
love than they can handle —\
through positive experiences with so many\
beautiful women they lose their awe\
of beauty and,  in turn\
,  their powerlessness under its spell\
. It will help you acquire\
the right frame of mind to\
stop using the words <em\
>hot,  cute,  gorgeous\
,  </em>or <\
em>beautiful </em>\
to describe girls who turn you\
on. Instead,  say to\
yourself “she’s interesting\
” or “she might be\
worth getting to know”. Never\
compliment a girl on her looks\
,  especially not a girl you\
aren’t fucking. Turn\
off that part of your brain\
that wants to put them on\
pedestals. Further advanced training to\
reach this state of unawed Zen\
transcendence is to sleep with many\
MANY attractive women (try to\
                       avoid sleeping with a lot\
\
                       of ugly women if you\
                       don’t want to\
                       regress). Soon,  a\
Jedi lover you will be.</\
p></blockquote>\
<p\
>Starting today,  stop flattering\
women&#8217;s looks\
,  whether out loud or in\
your head.</p>\
<\
p>3. Get into\
a line of work where you\
are ordering beautiful women to do\
your bidding.</p>\
<\
p>If you can&#\
8217;t get sex with\
hot babes,  the next best\
thing is authority. Fashion photographers\
are not known as casanovas for\
nothing.</p>\
<p\
>4. Hang out with\
hot girls when they&#8217\
;re wasted and pissing themselves\
and vomiting.</p>\
<\
p>This is a pretty\
good cure for one-itis\
. Don&#8217;t\
worry about supply. America is\
churning them out like cheap factory\
products lately.</p>\
<\
p>5. Never stop macking.</p>\
<p>The life of\
the lady&#8217;s\
man is always in forward motion\
. The day you slow down\
is the day you start misremembering\
your ex as hotter than she\
really was. By keeping women\
forever in your orbit,  by\
hitting on them day and night\
and year after year,  with\
intention or without,  you remind\
yourself of the corporeal,  earthly\
nature of women&#8217;\
s greatest asset,  of their\
insufferable and dispiriting interchangeability,  and\
your heart is steeled for the\
endless battle.</p>
'


gm9 = epub.EpubHtml(title='your training to delight women',
file_name='your_training_to_delight_women.xhmtl',
lang='en')
gm9.content='\
<h2>Your Training To\
Delight Women</h2>\
<\
p>Players and unaffiliated men\
who labor to pass on the\
Good Word of Game usually admonish\
neophytes that borderline uncomfortable numbers of\
approaches need to be made in\
order to become proficient at pickup\
. You&#8217;ve\
got to get out there and\
talk to more women than you\
would normally do in the course\
of a nondescript day.</p\
>\
<p>This message\
is a good one. You\
won&#8217;t get\
good at the crimson arts until\
you&#8217;ve put\
in some real world practice interacting\
with lots of different women.\
The exact number is irrelevant;\
whether it takes you ten or\
one thousand approaches to improve doesn\
&#8217;t change the\
undeniable reality that very few men\
have the ability to go from\
video gaming malaise to WunderJuan on\
their first approach.</p>\
\
<p>You could say\
that the approach mentality,  at\
least during the learning curve stage\
,  is a core principle of\
game.</p>\
<p\
>There&#8217;s\
one other core game principle that\
I don&#8217;t\
see mentioned very much,  if\
at all,  in the pickup\
literature. In my view,\
it&#8217;s just\
as important a principle as approaching\
girls enough times to trespass beyond\
your comfort zone. That principle\
is the &#8220;find\
and foment her flaws&#8221\
; theory.</p>\
<\
p>The idea is simple\
. Every woman you meet,\
from friend to love prospect to\
the barest acquaintance,  and every\
woman who crosses your field of\
visual inspection,  will be subject\
to your exceedingly judgmental eye.\
You will search,  find and\
declare to yourself her flaw or\
flaws. If propriety and privacy\
allows it,  you will verbalize\
her flaw so that it may\
become cemented in your wavering cortex\
and banish all doubt of the\
flaw&#8217;s authenticity\
. It is a well-\
kown fact among the big-\
toothed motivational speaker circuit that saying\
aloud slogans of self-encouragement\
or life goals helps the chanter\
sculpt corporeal heft to his dreams\
.</p>\
<p>\
So,  for example,  you\
see a woman in the mall\
riding an escalator. Her sundress\
flounces insouciantly from above you.\
An incipient boner stirs. But\
this time,  instead of allowing\
your beta twerpitude the run of\
your skullcase and straining to catch\
imagined glimpses of panty,  you\
silence the dork force and,\
with proud stentorian innerauthority,  jot\
a solid mental note of her\
larger-than-ideal thighs\
. Safe distance permitting,  you\
might even rumble in a dampened\
voice to yourself,  &#8220\
;Hm,  thunder thighs.\
Too much speckle.&#8221;</\
p>\
<p>You\
will enact this devious scheme for\
every attractive and not-so\
-attractive woman who has the\
misfortune of falling prey to your\
daggered gaze. Only the obvious\
sexual market losers of femaledom &#\
8212; the grossly obese,\
the crassly ugly,  the desiccated\
old &#8212; will be\
exempt,  for their flaws are\
so prominently obscene they need no\
reminding nor rooting.</p>\
\
<p>What is the\
purpose of Principle #2?\
To balance gender sheets?</p\
>\
<p>Certainly,\
you could argue with strong evidence\
that women are particularly unforgiving of\
men&#8217;s flaws\
,  in the private if not\
in the public,  being as\
how they are slaves to a\
much more powerful hypergamous force that\
excels at weeding out stellar-\
lite suitors with extreme prejudice.\
A little harsh judgment from you\
is just giving women a taste\
of the moldy bread they daily\
give to men.</p>\
\
<p>But,  no\
,  that&#8217;s\
not the purpose,  as vengefully\
titillating as that seems. The\
purpose is purely practical. The\
finding and fomenting of women&#\
8217;s flaws conditions the\
beta male mind to accept the\
attainability of women,  and to\
discard the reflexive sanctification of women\
. No master seducer who ever\
lived believed even one woman was\
unattainable by him,  nor that\
any woman was a flawless vessel\
of purity. The seducer loves\
women,  but his love is\
vast enough to revel in women\
&#8217;s flaws.\
And that is why he wins\
.</p>\
<p>\
The beta male who conditions himself\
thus,  by his efforts to\
discover the flaws in women kept\
hidden to him by the shadow\
of his turgid lust cast around\
his vision,  will slowly feel\
the power and the strength of\
<a href="https://\
heartiste.wordpress.com/\
2012/03/08/\
the-aloof-alpha-\
attitude-explained/" target="\
_blank">the Attitude</a\
>,  that indomitable voice that rises\
like the Great Scrotum from the\
pubic patch and delivers with valedictorian\
presumption the message that no woman\
is out of reach or free\
of exploitable insecurities,  the exploiting\
of which by a savvy man\
she herself would be ashamed to\
admit thrills her to the clitbone\
.</p>\
<p>\
Returning to escalator girl,  here\
are some more examples of flawmobbing\
.</p>\
<p>&#\
8211; skewed eyes<br\
/>\
&#8211; narrow hips\
<br />\
&#8211;\
rumpled blouse<br />\
&#\
8211; misshapen boobs<br\
/>\
&#8211; nip/\
tuck victim<br />\
&#\
8211; manhands<br />\
\
&#8211; roo pouch<\
br />\
&#8211; clown\
feet<br />\
&#8211\
; incipient hump<br />\
\
&#8211; jug ears<\
br />\
&#8211; wasted\
calves<br />\
&#8211\
; bow-legged<br\
/>\
&#8211; flabby arms\
<br />\
&#8211;\
pigeon-toed<br />\
\
&#8211; broad shouldered<\
br />\
&#8211; excessive\
peach fuzz<br />\
&#\
8211; asymmetric nostrils<br\
/>\
&#8211; ETC</\
p>\
<p>I\
can already hear the gripers.\
&#8220;But I just\
saw the hottest chick ever and\
she looked PERFECT! I couldn\
&#8217;t find anything\
wrong with her.&#8221;</\
p>\
<p>There\
is always something wrong with a\
girl,  no matter how beautiful\
. You may have to dig\
a little deeper,  but you\
&#8217;ll find her\
thermal exhaust port with a practiced\
keen eye. Note that any of the above can easily apply\
to the hottest girl you have\
ever seen. That&#8217\
;s the beauty of the\
flawfinding mission: it unearths the\
normally overlooked blemishes scattered among a\
girl&#8217;s mien\
that her general beauty tends to\
obscure to men. If you\
socialize with a girl and gain\
insight into her personality,  you\
have even more data from which\
to devise withering,  silent judgments\
.</p>\
<p>\
Once you have gotten reliable at\
noticing and promoting women&#8217\
;s flaws,  their beauty\
will no longer hold such paralyzing\
power over you. Conditioned to\
emphasize a woman&#8217;\
s worst and attenuate her best\
,  you will become a cad\
machine,  irresistible to the fairer\
sex who will react shaken from\
their stupor by your dispassionate demeanor\
and feel the threat of your\
pervasive critical eye with senses aflame\
.</p>\
<p><\
strong>Maxim #30:\
Ignore a woman&#8217;\
s flaws at your peril.\
They are the key to reconfiguring\
your perception,  and thus her attainability.</strong></p>
'


gm10 = epub.EpubHtml(title='screening girls',
file_name='screening_girls.xhtml',
lang='en')
gm10.content='\
<h2>Screening Girls</h2>\
<p>Women choose,  \
men are chosen. This is \
the basic tenet of evolutionary mate \
selection. So does this mean \
there is nothing men can do \
to put more power in their \
own hands? Absolutely not. \
Paradoxically,  the role of being \
chooser has made women susceptible to \
men acting as the chooser. \
A man who chooses women,  \
whether in reality or perception,  \
signals he is high value to \
a woman. This is why \
schools of seduction teach the importance \
of <a href="https\
://heartiste.wordpress.com\
/2008/04/30\
/qualifying-her/" target\
="_blank">&#8220;qualifying\
&#8221;</a>. Girls \
will say they don&#8217\
;t want to be lined \
up like cattle and chosen by \
men,  but in practice they \
secretly yearn for a man to \
have standards and ruthlessly apply them\
,  in the same way they \
do to men. A woman \
loves to feel special that her \
man chose her over other options \
he had&#8230; until \
he dumps her for a hotter \
chick.</p>\
<p\
><img class="alignleft size\
-large wp-image-\
1562" title="img_01421" \
src="https://heartiste.\
files.wordpress.com/\
2008/10/img_01421.\
jpg?w=500&#\
038;h=375" \
alt=""   />In light of \
this fact of female nature,  \
here are some screening tests you \
could apply to women you are \
dating. You don&#8217\
;t have to believe in \
all of your high standards,  \
you just have to act like \
you do. For instance,  \
I don&#8217;t \
really care if a woman <\
span style="text-decoration\
:line-through;">has \
banged guys in different cities around \
the world</span> likes \
to travel,  but I qualify \
her as if this was critically \
important to my continuing interest in \
her.</p>\
<p\
>&#8220;The last girl \
I dated was very provincial. \
I&#8217;m a \
mentally active man who challenges himself\
,  and I can&#8217\
;t be with someone who \
won&#8217;t join \
me in my adventures. So \
are you the adventurous type who \
seeks new experiences?&#8221;</\
p>\
<p>She \
will now be like putty in \
your hands,  insisting she LOVES \
to travel and enjoys learning about \
new cultures. Segue into pussy \
pounding.</p>\
<p\
>Fake your high standards until \
you are banging enough quality pussy \
that you have internalized your high \
standards. At that point,  \
not only will you be dumping \
chicks for major infractions like lying \
and dullness and weight gain,  \
you&#8217;ll be \
dumping them for minor things like \
owning too many shoes.</p\
>\
<p><span style\
="text-decoration:underline\
;">Examples</span></p\
>\
<p>Screening her \
for anti-marriage beliefs:</\
p>\
<p>You\
: One thing that&#8217\
;s important to me is \
that the girl I&#8217\
;m with doesn&#8217\
;t feel pressured to conform \
to societal expectations. She has \
her own mind and values her \
independence. She&#8217;\
s cool with loving,  long \
term relationships that don&#8217\
;t need to be validated \
by a Justice of the Peace\
.</p>\
<p>\
Screening her for loathing of children\
:</p>\
<p>\
You: When you see a \
cute little kid snotting himself in \
the mall and rubbing his germs \
all over everything,  what do \
you think? They&#8217\
;re such a responsibility that \
saps life of all its joy\
,  would you agree?</p\
>\
<p>Screening her \
for generosity:</p>\
<\
p>You: Do you \
know how to give a good \
backrub?</p>\
<p\
>Screening her for fidelity:</\
p>\
<p>You\
: What do you feel about \
guys who like to keep their \
options open and date around until \
they find that perfect match?</\
p>\
<p>(Note\
    : This is reverse psychology\
    . The more she hates \
    on guys who date around\
    ,  the likelier it is \
    she is doing the same\
    .)</p>\
<p\
>Screening her for wife and \
mother potential:</p>\
<\
p>You: I really \
like girls who have a crazy \
streak and no hang-ups\
. Have you ever let a \
guy snort coke off your ass\
?</p>\
<p>\
Screening her for sluttiness:</p\
>\
<p>You: \
    On a scale from 1 \
    to 10,  how would \
    you rate your blowjob technique\
    ?</p>\
<p\
>Screening her for femininity:</\
p>\
<p>You\
: Have you ever,  or \
are you now,  working for \
a law firm in any capacity \
or going to law school?</\
p>\
<p>Screening \
her for romanticism:</p>\
\
<p>You: I \
like girls who can have a \
great time with me spending no \
money just walking around the tidal \
pool at midnight and staring at \
the stars in the sky. \
(Wait for her reaction. \
 If she&#8217;\
 s a money or status \
 whore,  you&#8217\
 ;ll see a quick \
 flash of disgust cross her \
 face before she settles on \
 the appropriate answer.)</p\
>\
<p>Screening her \
for willingness to please you:</\
p>\
<p>You\
: I can only be with \
a girl who likes to exercise\
,  not one who sees it \
as a chore.</p>\
\
<p>******</p>\
<\
p>These screening tests should \
get you started. If you\
&#8217;re looking to \
just get laid,  you&#\
8217;ll want to toss \
softballs and screen her for things \
she is eager to confirm &#\
8212; like love of travel\
. For girlfriend screenings,  you\
&#8217;ll want to \
bang her first,  then apply \
more vigorous screens to weed out \
those girls who would be a \
waste of your resources.</p\
>\
<p>But the \
best screening test I&#8217\
;ve found BY FAR is \
looking at a picture of her \
mother &#8212; there&#\
8217;s your future,  \
buddy. Choose wisely.</p
>
'


gm11 = epub.EpubHtml(title='top thinking about the next girl',
file_name='next_girl.xhtml',
lang='en')
gm11.content='\
<h2>Don''t Stop Thinking About The Next Girl</h2>\
<p>A big mistake guys make when they start \
dating a girl they really like \
&#8212; the &#8220\
;one&#8221; &#\
8212; is neglecting to continue \
going out and getting fresh leads\
.  I used to do this\
,  so I know the mental \
processes that go through a guy\
&#8217;s head when \
he&#8217;s really \
into a girl he&#8217\
;s dating.  He channels \
all his pickup energy into this \
one girl,  figuring that if \
he made it as far as \
a first or a second date \
he should focus like a laser \
beam on her pants zipper.  \
He spends the long days in \
between seeing her analyzing his progress\
,  picking apart the meaning behind \
her actions (or inactions),  \
and daydreaming about what a relationship \
would be like with her.  \
When he goes out,  he \
gets lazy and tells himself there \
is no urgency to collect new \
numbers since he&#8217;\
s already dating a quality chick \
and most of the other girls \
can&#8217;t compare \
anyhow.</p>\
<p\
>This is a sexually lethal \
frame of mind to put oneself \
in.  When a guy completely \
boxes himself in like this with \
no options to fall back on\
,  all it takes is a \
change of heart by his golden \
girl to crush his soul and \
send him spiraling into morose self\
-examination.  It&#8217\
;s like investing your whole \
wad in a biotech startup with \
huge promise only to see it \
crash to a sub-penny \
stock after the CEO is convicted \
of fraud.  You&#8217\
;d have been a lot \
better off diversifying your portfolio in \
a range of pussy sectors.</\
p>\
<p>As \
an example,  once,  during \
the course of a month,  \
I had four second dates in \
a row fizzle out on me \
leading to no sex.  I \
made a critical error by jumping \
from one girl to the next \
&#8212; dating,  failing\
,  getting a new lead,  \
dating again,  failing again,  \
etc.  My desperation and self\
-doubt grew with each new \
girl,  practically ensuring failure.</\
p>\
<p>The \
way to beat this crippling dating \
handicap is to follow the &#\
8220;two in the kitty\
&#8221; rule religiously.  \
You should date a minimum of \
two girls simultaneously until you have \
locked in your preferred girl by \
having sex with her at least \
three times.  I have found \
through trial and error that a \
girl will bond to you after \
the third bang.  Before that\
,  it&#8217;s \
a crapshoot and depends on the \
girl&#8217;s innate \
femininity.  Because modern girls have \
taken on male characteristics (especially \
                               DC girls who are more \
                               masculine than girls from less \
                               ambitious or overeducated towns) \
and are sluttier than past generations\
,  the first or second bang \
won&#8217;t guarantee \
emotional attachment.  By the third \
bang,  however,  you will \
notice a very perceptible shift in \
the balance of power.  Suddenly\
,  she will call and text \
you first,  ask about your \
weekend schedule,  tell you to \
&#8220;give me a \
call soon&#8221;,  start \
doing favors for you,  cuddle \
longer,  and generally betray signs \
of nervousness when you make yourself \
physically or emotionally scarce.</p\
>\
<p>That is \
when you will have her in \
the palm of your hand and \
can steer the relationship in the \
direction you want it to go\
.</p>\
<p>\
A guy can achieve this if \
he adheres to these fundamental principles\
:</p>\
<ol>\
\
<li>Other girls CAN \
compare.  Girls are more interchangeable \
than you&#8217;d \
think.  Don&#8217;\
t get sucked into &#8220\
;oneitis&#8221;.</li\
>\
<li>If you \
date one girl exclusively and she \
really turns you on,  you \
WILL give off a needy vibe \
at some point during the pre\
-sex seduction no matter how \
much experience you have.  The \
best players who have ice running \
through their veins and cyborgian state \
control get that way because they \
date and fuck many girls concurrently\
.</li>\
<li>\
A good date means nothing.  \
The only thing that matters is \
penis in vagina,  and even \
then a feeling of security is \
not assured until the penis has \
penetrated the vagina on at least \
three different occasions.  (Three \
                             times in one night does \
                             not count.)</li>\
\
<li>You will find \
it easier to close the deal \
with your number one girl if \
you are banging a number two \
and three girl.  A man \
getting regular sex has an aura \
that girls subconsciously register in their \
hindbrains.  Don&#8217;\
t ask me how this happens\
,  but it does.  The \
<strong>Aura</strong\
> is very powerful,  like \
the chemical hormones secreted by ants \
and bees to get them to \
cooperate as a social structure,  \
and will be your <a \
target="_blank" href="\
http://en.wikipedia.\
org/wiki/Valkyrie">\
Valkyrie</a> in the \
battle for pussy.</li>\
\
<li>Approach the game \
while dating as ardently as you \
do when you are dating no \
one.  If you have a \
date Tuesday,  go out Monday \
and Wednesday and get more numbers\
.  Even if you fail at \
getting numbers,  just taking the \
initiative of meeting new girls and \
chatting them up will reduce the \
neediness you feel with your date\
.</li>\
<li>\
Never,  EVER,  feel guilty \
for dating and banging many girls \
simultaneously.  The mating marketplace is \
a battlefield and the Genitalia Convention \
rules of engagement clearly stipulate that \
it&#8217;s open \
season for fucking around until terms \
of exclusivity are tendered.  This \
is not your mother&#8217\
;s dating environment.</li\
>\
<li>A hot \
chick is MORE likely,  not \
less,  to continue seeing you \
if you tell her you are \
&#8220;dating around&#\
8221;.  A guy who knows \
he has options and is in \
fact exercising those options is extremely \
attractive to a girl.</li\
>\
</ol>\
<p\
>Don&#8217;t \
give a girl the chance to \
pull the rug out from under \
you.  Have another ten rugs \
underneath that one and you will \
glide through your interactions with women \
like a shark through a school \
of mackerel.</p>
'


gs = epub.EpubHtml(title='body language',
file_name='body_language.xhtml',
lang='en')
gs.content='\
<h2>Body Language</h2>\
<p>This is where\
the majority of guys stumble during\
the pickup.  The first impression\
is made within seconds,  on\
the walk over to the girl\
,  before one word is spoken\
.  The way a guy carries\
himself,  moves his body,\
his hands and arms,  positions\
his feet,  stands,  maintains\
eye contact,  and interacts non\
-verbally with girls is half\
his game.  You can spit\
the words of Voltaire,  but\
if your body is incongruent with\
what you&#8217;re\
saying,  you will get blown\
out.</p>\
<p\
>Some of the common beta\
body language mistakes I see guys\
making:</p>\
<ul\
>\
<li><strong>\
Walking over to the girl too\
quickly</strong></li>\
\
</ul>\
<p>\
When a guy sees a cute\
chick he gets excited.  His\
adrenaline pumps and his heart races\
as he thinks about how best\
to approach her.  This inner\
turmoil reveals itself in his physical\
composure.  He marches toward her\
too fast,  propelled by his\
unspoken insecurity to get the job\
over with as soon as possible\
.  Fast walkers are unattractive.\
Focus on your walking speed.\
Stroll over like a pimp taking\
his time to admire the other\
girls in the room along the\
way.</p>\
<ul\
>\
<li><strong>\
Doing everything too fast</strong\
></li>\
</ul>\
\
<p>Related to the\
above,  guys tend to gesticulate\
too rapidly when they get nervous\
,  reflexively jerking around their hands\
,  arms,  and head.\
Be aware of this and deliberately\
slow down all your movements.\
Take an extra two seconds to\
reach for a beer.  Move\
around her in languid,  measured\
rhythms.  When she is speaking\
,  slowly cock your head to\
the side.  The key thing\
is to avoid any sudden movements\
.  That betrays anxiety.  It\
helps to imagine your life is\
a movie in slo-mo\
.</p>\
<ul>\
\
<li><strong>Being\
too stiff</strong></li\
>\
</ul>\
<p\
>The opposite of the above\
is when a guy stiffens up\
from nerves.  Don&#8217\
;t be a totem pole\
.  Move your arms around,\
swivel your body,  make hand\
gestures while telling a story.\
Watch Marlon Brando in The Godfather\
.  Just do it all slowly\
.</p>\
<ul>\
\
<li><strong>Closed\
body language</strong></li\
>\
</ul>\
<p\
>Guys who are confident that\
nothing in life can touch them\
have very open and smooth body\
language.  Nervous guys who are\
always afraid of fights,  of\
being sucker punched,  of conflict\
,  will defensively scrunch up their\
body as if they were psychologically\
warding off blows.  Guys who\
fear nothing open their arms,\
expose their chests,  and generally\
project the look of someone who\
never worries about being caught off\
-guard.  In that vein\
,  avoid shoving your hands in\
your pockets,  crossing your arms\
,  standing with a narrow stance\
,  looking around the room with\
darting eyes,  slouching,  or\
grabbing one forearm with your hand\
.</p>\
<ul>\
\
<li><strong>Holding\
drinks too high</strong></\
li>\
</ul>\
<\
p>Very common.  Don\
&#8217;t do it\
.  Look at old James Bond\
films.  Sean Connery holds his\
tumbler down by his waist,\
not up by his nipples.</\
p>\
<ul>\
<\
li><strong>Adjusting himself\
</strong></li>\
</\
ul>\
<p>Any\
primping should be done at home\
before going out.  Don&#\
8217;t tug at your\
cuffs,  flatten your hair,\
pick at your fingernails,  swipe\
at your nose,  rub your\
eyes,  brush off imaginary lint\
,  or hoist your pants.\
A relaxed alpha male does not\
primp in the field.</p\
>\
<ul>\
<li\
><strong>Leaning in (\
    pecking)</strong></li\
>\
</ul>\
<p\
>Another common mistake.  Nearly\
every guy does this when starting\
out.  It&#8217;\
s called pecking because the motion\
of jerking your head and body\
forward to listen with rapt attention\
to what a girl is saying\
looks like a chicken pecking at\
seed.  She is not so\
important that you need to lean\
in to catch every precious word\
.  Lean back with your whole\
body and let her lean into\
you.  If she has something\
to say she&#8217;\
ll move in so you can\
hear it.  The act of\
bending to your will fires up\
her loins.  The one exception\
is in very noisy venues where\
you have to lean in if\
she is a soft talker.\
It&#8217;s OK\
to do this as long as\
you lean in SLOWLY and lean\
back during pauses.</p>\
\
<ul>\
<li><\
strong>Weak eye contact</\
strong></li>\
</ul\
>\
<p>Hold it\
slightly longer than you feel comfortable\
doing.  Dominating another guy with\
steady eye contact can lead to\
a fight.  Dominating a girl\
with eye contact can lead to\
sex.  Remember,  girls WANT\
to feel dominated.  It turns\
them on.  And making sure\
she breaks eye contact first is\
a great way to demonstrate dominance\
.</p>\
<ul>\
\
<li><strong>High\
pitched,  incessant fast talking</\
strong></li>\
</ul\
>\
<p>A guy\
who is seeking approval will talk\
fast,  hoping to finish his\
point before people become bored with\
what he&#8217;s\
saying.  His tone of voice\
will rise as sentences are completed\
.  A guy who is confident\
that everyone will listen intently to\
his brilliance will talk slowly in\
a low or neutral pitch and\
pause frequently.  Pausing is an\
extremely powerful method of subcommunicating dominance\
.  Think about a really effective\
professor or manager.  They begin\
speaking&#8230; PAUSE to\
build anticipation&#8230; make\
their point&#8230; PAUSE\
to let it sink in&#\
8230; conclude&#8230;\
PAUSE again&#8230; for\
effect.  The words don&#\
8217;t matter as much\
as how you say them.</\
p>\
<ul>\
<\
li><strong>Beta body\
positioning</strong></li>\
\
</ul>\
<p>\
After the approach,  guys usually\
remain standing at the point they\
first entered the group to introduce\
themselves.  This spot is often\
on the outside of the social\
circle,  back to the crowd\
,  looking in at his target\
.  That is a weak position\
.  You want to move to\
the power position as quickly as\
possible.  The power position is\
center of the group,  back\
to the wall or the bar\
,  facing the room as if\
you were a king surveying your\
kingdom and your subjects were gathered\
round to entertain you.  A\
trick for maneuvering to the power\
position is to take a girl\
&#8217;s hand,\
lift it up so she reacts\
by doing a spin move,\
and spinning her away from the\
bar.  You then steal her\
spot or chair.  You can\
even call attention to your bold\
move:  &#8220;Oh\
man,  I just stole your\
seat!&#8221;</p>\
\
<ul>\
<li><\
strong>Poor stance</strong\
></li>\
</ul>\
\
<p>If you are\
standing,  keep your feet apart\
close to the width of your\
shoulders.  An alpha monopolizes space\
.  One foot should point forward\
and the other should point outward\
about 45 degrees.  Thrust your\
pelvis out slightly.</p>\
\
<ul>\
<li><\
strong>Poor sitting</strong\
></li>\
</ul>\
\
<p>If you are\
sitting,  don&#8217;\
t cross your legs.  You\
&#8217;re not an\
old man.  Spread them out\
as if you were naked and\
you wanted the whole world to\
behold your breathtaking package.</p\
>\
<ul>\
<li\
><strong>Showing his palms too frequently</strong></li>\
</ul>\
<p>This non-\
verbal faux pas is a little\
arcane,  but subconsciously girls notice\
it.  Turning your hands up\
is a sign of submission.\
In the beginning,  when you\
are building attraction by demonstrating your\
alphaness you should keep your palms\
down or turned inward.  Emphasize\
points by raising and lowering your\
hand,  palm down.  If\
you look at video clips of\
presidential candidates on the stump you\
will see that the force of\
their speaking is intensified by strong\
hand movements.  Bill Clinton often\
addressed the crowd with his palm\
in,  fingers curled into a\
fist,  and thumb pointing out\
like a gun.  Later,\
during the comfort stage of the\
pickup after she is attracted,\
you can show your palm to\
display vulnerability.</p>\
<\
ul>\
<li><strong\
>Forgetting to touch the girl\
</strong></li>\
</\
ul>\
<p>This\
one is huge.  Probably the\
number one alpha trait is comfort\
with touching other people.  A\
guy totally gives away his betatude\
if he is uncomfortable touching girls\
.  Touching should start immediately,\
literally within two seconds of the\
approach.  During your introduction,\
lightly touch your target and the\
potential cockblock on the elbows simutaneously\
.  Start inoffensively,  like on\
the forearms or shoulders,  then\
gradually move to touching more erogenous\
zones,  like the upper back\
,  upper arm,  or thigh\
.  Avoid accidentally touching the bra\
strap,  the hair,  or\
the face too soon,  as\
these spots will fire off an\
instant recoil reaction in a girl\
who isn&#8217;t\
yet attracted to you.  When\
you talk in her ear take\
advantage of the moment to graze\
her cheek with yours.  The\
small of the lower back is\
a highly charged zone,  so\
move your hand down her back\
as the pickup progresses.  Wrap\
your arms around her waist when\
you want to move her to\
another location in the bar.\
Anytime you say something funny,\
anchor it with your touch.\
When I have a good pickup\
my hands RARELY break contact with\
my target.</p>\
<\
ul>\
<li><strong\
>Not smiling or smiling at\
the wrong times</strong></\
li>\
</ul>\
<\
p>Yep,  pretty basic\
.  Always smile on the approach\
.  Just don&#8217;\
t overdo it.  Drop the\
smile after your introduction.  Smiling\
and laughing works best in measured\
doses.  NEVER laugh at your\
own jokes.  Don&#8217\
;t laugh everytime she says\
something funny.  Your attitude should\
be <em>&#8220;\
Oh she said something adorable again\
.  How cute!&#8221;</\
em>,  not <em>&#\
8220;HA HA this girl\
is the funniest!  She is\
SO cool!  She is the\
best!&#8221;</em>\
Alternating your smiling with smirking,\
frowning,  and a straight face\
is the winning formula.</p\
>\
<ul>\
<li\
><strong>Animated facial gesturing\
</strong></li>\
</\
ul>\
<p>In\
the early stages of the pickup\
when you are bringing higher energy\
than your target in order to\
get attraction it&#8217;\
s acceptable to accentuate your stories\
with facial gestures.  Later on\
,  though,  you want to\
avoid these histrionics.  Constantly raising\
your eyebrows,  nodding your head\
,  widening your eyes,  smiling\
broadly,  or twisting your mouth\
into funny shapes indicates an approval\
seeking mentality.  You are not\
an approval seeker,  you are\
an approval giver.</p>\
\
<ul>\
<li><\
strong>Moving out of the\
way to accommodate others</strong\
></li>\
</ul>\
\
<p>Hold your ground\
.  When a guy needs to\
pass by,  make him move\
around you.  You don&#\
8217;t want to be\
that guy who&#8217;\
s always stepping out of the\
way to avoid getting jostled by\
the crowd.  When a girl\
reaches for her drink,  make\
her go over or around you\
.</p>\
<ul>\
\
<li><strong>Facing\
the girl directly</strong></\
li>\
</ul>\
<\
p>Don&#8217;\
t face your target directly until\
after she has qualified herself to\
you.  She does not deserve\
your full attention when you first\
meet her.  Keep your body\
angled slightly away from her.\
Later,  when she has earned\
your interest,  turn to face\
her completely.  This is the\
signal to move into rapport.\
Note:  If you are running\
direct game you will face her right away.</p>\
<p>Go forth,  and lubricate vaginas with the power of your presence.</p>\
'

gs2 = epub.EpubHtml(title='alpha body language',
file_name='alpha_body_language.xhtml',
lang='en')
gs2.content='\
<h2>Alpha Body Language\
</h2>\
<p>\
In my view,  and in\
the view of much of the\
seduction community,  the single biggest\
factor of early game success is\
body language. Women react viscerally\
to a man&#8217;\
s strong body language before he\
has said one word. The\
way he walks toward her,\
the way he smiles,  the\
<a href="https://\
heartiste.wordpress.com/\
2008/10/15/\
standing-like-an-\
alpha/" target="_blank">\
way he stands</a>.\
It strikes me that the reason\
this is so is because it\
is harder to fake the subtle\
indicators of alphaness with your body\
than it is with your words\
. Women have evolved to be\
perceptive of a man&#8217\
;s emotional state and body\
language is the physical manifestation of\
inner game,  so that&#\
8217;s what women key\
in on first.</p>\
\
<p>I have <\
a href="https://heartiste\
.wordpress.com/2009\
/03/02/anti\
-game/" target="_blank\
">written some posts</a\
> on how to spot <\
a href="https://heartiste\
.wordpress.com/2008\
/10/02/what\
-you-can-learn\
-from-a-beta\
/" target="_blank">beta\
body language</a> and\
how to mimic <a href\
="https://heartiste.wordpress\
.com/2008/08\
/21/spot-the\
-alpha/" target="_blank\
">alpha body language</a\
>. One of the most important\
points I have made is that\
it is imperative you avoid <\
a href="https://heartiste\
.wordpress.com/2007\
/11/20/body\
-language/" target="_blank\
">jerky,  reactive movements</\
a>. Well,  the science\
is rolling in and,  unsurprisingly\
to anyone who has lived a\
day in his life and finds\
corroborating evidence in what I write\
,  the <a href="\
http://www.cosmosmagazine.\
com/news/2771/\
wimps-have-faster-\
reaction-time" target="\
_blank">conclusions are vindicating</\
a> my worldview.</p\
>\
<blockquote><p>\
Wimps have rapid reaction times</\
p>\
<p>OREGON\
,  U.S.: Unfit\
or weak people react sooner to\
sounds of approaching danger than strong\
,  healthy people – which may\
be an evolutionary adaptation to allow\
them a larger margin of safety\
,  says a new study.</\
p>\
<p>Test\
subjects listened to a sophisticated sound\
system that mimicked an approaching object\
,  explained John Neuhoff,  an\
evolutionary psychologist at the College of\
Wooster in Ohio,  U.\
S.,  and co-leader\
of the study.</p>\
\
<p>The &#8216\
;virtual object&#8217;\
sounded like a motorcycle passing on\
a highway,  approaching the subject\
at 15 m/s and\
then whizzing past them. The\
subjects were asked to hit a\
key when they thought the sound\
was right in front of them\
.</p>\
<p>\
Fitness was measured by two variables\
: heart rate after a bout\
of moderate cardiovascular exercise and muscular\
power,  measured by the strength\
of their hand grips. [&#\
                      8230;]</p>\
<\
p><strong>&#8220;\
It&#8217;s beneficial\
[for the weaker] to\
react sooner rather than later,\
&#8221;</strong> said\
Neuhoff. &#8220;The\
cost of responding too early is\
far less than the potentially fatal\
cost of responding too late.&#\
8221;</p></blockquote>\
\
<p>Corollary: It\
&#8217;s beneficial for\
the stronger to take their sweet\
time reacting to events. Not\
because it will lessen his chances\
of getting killed (mauled or\
                   bludgeoned in the ancestral environment\
                   ),  but because women are\
wired to associate a calm demeanor\
and stoic repose with an alpha\
male she wants to fuck.</\
p>\
<blockquote><p\
>Women typically responded sooner than\
men,  who on average are\
physically stronger.</p></blockquote\
>\
<p>This is\
evidence that beta males behave more\
like women than men. No\
wonder they get LJBFed.</p\
>\
<p><a href\
="http://www.nature\
.com/news/2009\
/090602/full/news\
.2009.537.html\
" target="_blank">Here\
is another study</a>\
proving the efficacy of my body\
language advice.</p>\
<\
blockquote><p>Women become\
less choosy when they,  rather\
than men,  move from table\
to table. [&#8230;]</\
           p>\
<p>\
           A study in Psychological Science\
           points out that chivalric behaviour\
           created by the speed-\
           dating experience may be skewing\
           the data.</p>\
\
           <p>Normally in\
           speed dating,  men walk\
           around a room and visit\
           a succession of seated women\
           for mini dates just a\
           few minutes long. Later\
           ,  the participants note down\
           whom they would like to\
           meet again. If there\
           is a match,  the\
           organizers help the people to\
           get in touch. Psychologists\
           have found that although men\
           choose,  on average,\
           half of the women present\
           ,  women choose to see\
           only a third of the\
           men again.</p>\
\
           <p>This isn\
           &#8217;t really\
           a surprise. Among animals\
           ,  females are usually the\
           picky ones,  because they\
           make the larger reproductive investment\
           . However,  the new\
           research,  by Eli Finkel\
           and Paul Eastwick,  social\
           psychologists at Northwestern University in\
           Evanston,  Illinois,  demonstrates\
           that tinkering with the speed\
           -dating format alters human\
           behaviour,  dramatically changing the\
           outcome. [&#8230;]</\
                     p>\
<p>\
                     The researchers established 15 speed\
                     -dating events for 350\
                     young adults. During eight\
                     events,  men rotated around\
                     the seated women,  and\
                     during seven events,  women\
                     moved between seated men.\
                     When men rotated,  men\
                     said yes 50% of\
                     the time and women said\
                     yes 43% of the\
                     time. However,  when\
                     women rotated,  the trend\
                     for higher female selectivity vanished\
                     ,  with men saying yes 43% of the time while women said yes 45% of the time.</p></blockquote>\
<p>I have long contended that one of the reasons\
                     <a href="https\
                     ://heartiste.wordpress.\
                     com/2008/05\
                     /29/speed-\
                     dating-sucks/" target\
                     ="_blank">speed dating\
                     sucks</a> (\
                         besides the surfeit of cougars\
                     ) has to do with\
                     the retarded system organizers use\
                     requiring men to be the\
                     ones to switch tables while\
                     the women remain seated.\
                     This dynamic creates the impression\
                     that the men are slabs\
                     of meat in a butcher\
                     &#8217;s display\
                     case that women casually browse\
                     for the choicest cuts.\
                     It exacerbates an already lopsided\
                     intrinsic mating market mechanism.</\
                     p>\
<blockquote><\
                     p>The researchers think\
                     the reason for this phenomenon\
                     is related to embodiment —\
                     <strong>the idea\
                     that physical actions can alter\
                     perception.</strong> Pulling\
                     something closer makes the object\\
                     being pulled more appealing,\
                     whereas pushing something away makes\
the object less desirable.</p\
>\
<p>Finkel and\
Eastwick argue that approaching someone makes\
the mind want what it is\
approaching,  because people are in\
the habit of moving towards objects\
that they want and moving away\
from objects that they don&#\
8217;t want.</p\
></blockquote>\
<p>\
Alpha body language,  gentlemen.\
Learn it. It works and\
it&#8217;s a\
lot easier to integrate into who\
you are than is memorizing a\
long-winded routine. The\
above study proves that the ideal\
alpha position is back against the\
bar,  looking outward and surveying\
your kingdom as girls approach from\
all directions. The study also\
reinforces the widely held PUA belief\
that indirect approaches are more optimal\
than direct approaches. Perhaps this\
is why the over-the\
-shoulder,  &#8220;\
just passing through&#8221;\
approach coupled with a time constraint\
works so well. You are\
mimicking in vibe and energy,\
as best you can while in\
motion,  the man sitting down\
at a speed dating event while\
rotating women walk up to his\
table to earn the pleasure of\
his company.</p>\
<\
p><span style="text\
-decoration:underline;">Body\
language tips</span></p\
>\
<p>When a\
woman tries to get your attention\
,  take a second longer to\
swivel your head to reply.\
The goal is to introduce a\
palpable,  but not off-\
putting,  tension to the interaction\
. In other words,  make\
her sweat.</p>\
<\
p>Keep your head cocked\
upward slightly. This will accentuate\
the heaviness of your brow ridge\
and the heft of your chin\
and jaw,  both indicators of\
alpha testosterone levels. It also\
imparts you with a haughtiness that\
women find irresistible.</p>\
\
<p>Scratch your balls\
in public once in a while\
.</p>\
<p>\
If you say something stupid,\
goofy or impolite (hey,\
                   it happens) don&#\
8217;t backpedal or get\
flustered. Act as if nothing\
is wrong. Embarrassment is for\
the little people.</p>\
\
<p>Be scandalous.</\
p>\
<p>Rudely\
glance around the room every so \
often when a girl is talking \
to you.</p>\
<\
p>Be inattentive. Betas \
focus like a laser beam when \
engaging a girl because she is \
the reason for his existence. \
Alphas exist for themselves.</p\
>\
<p><strong>\
Maxim #17: Be narcissistic\
. There is no greater divergence \
than that between a woman&#\
8217;s stated disapproval of \
male narcissism and the rapidity with \
which she jumps into bed with \
a male narcissist.</strong></\
p>\
<p>Keep \
a toothpick in your mouth if \
you don&#8217;t \
smoke.</p>\
<p\
>Be judgmental. Say &#\
8220;Hm&#8221; \
and &#8220;I see\
&#8221; a lot when \
a woman talks to you,  \
arching your eyebrows and frowning skeptically\
.</p>\
<p>\
If a girl says something genuinely \
funny (rare,  like a \
       lunar eclipse),  don&#\
8217;t boisterously laugh in \
appreciation. Snicker instead.</p\
>\
<p>Be territorial\
. Spread those arms and legs \
out.</p>\
<p\
>Learn to love the pregnant \
pause. When a girl shit \
tests you,  don&#8217\
;t respond like a wind\
-up beta. Give her \
a blank,  serial killer stare \
and wait&#8230; wait\
&#8230;&#8230;. waiiiiit \
for it&#8230;. ANSWER\
! Wow,  that was hot\
. I&#8217;m \
positive I just made a female \
reader squirm delightfully in her seat\
.</p>\
<p>\
If you don&#8217;\
t have a witty answer ready \
for deployment,  silence beats stilted \
conversation.</p>\
<p\
>Lead with your crotch.</\
p>\
<p>Don\
&#8217;t ever fall \
for the &#8220;tap \
on the shoulder&#8221; \
or the &#8220;something \
on your tie&#8221; \
gags.</p>\
<p\
>Be imperious. The world \
is your harem.</p>\
<p>Finally&#\
8230; use the power \
of your back. Turning \
your back on people who \
have displeased you is a \
great way to get them \
to qualify themselves. Girls \
will reopen. Guys will vamoose.</p>
'


gs3 = epub.EpubHtml(title='just say something',
file_name='just_say_something.xhtml',
lang='en')
gs3.content='\
<h2>Just Say Something</h2>\
<p>You&#8217\
;re standing in front of\
a cute girl at the supermarket\
check-out line. You\
put the food on the conveyor\
belt,  stealing glances at her\
as she fiddles with her phone\
. She looks up briefly at\
you,  then looks back down\
. You want to say something\
,  anything halfway clever,  to\
get her smiling and a conversation\
rolling,  with the ultimate intention\
of a phone number exchange,\
or even,  dare you ponder\
it!,  an insta-date\
to the nearest coffee shop.</\
p>\
<p>But\
the moment evaporates silently,  your\
mouth paralyzed except for the &#\
8220;I don&#8217\
;t need a bag&#\
8221; you say to the\
cashier. Another wasted opportunity.\
But you brush it off easily\
as soon as you are out\
the door,  figuring you have\
years ahead of you and plenty\
of chances to meet girls in\
similar situations down the road.</\
p>\
<p>The\
next day,  you fumble another\
opportunity with a girl pumping gas\
next to you at the gas\
station. And again,  you\
glibly excuse your inaction with the\
comforting thought that years of opportunities\
await you.</p>\
<\
p>The same scene in\
different contexts is repeated&#8230\
; until those years have passed\
and the glib excuses don&#\
8217;t come so easily\
anymore. Regret weighs on you\
like a stone hung around your\
neck.</p>\
<p\
>***</p>\
<p>\
Does the above describe you?\
If you are like most men\
,  it does,  too often\
for your liking. There are\
many sticking points in game,\
from meeting to sex to relationship\
,  but the one sticking point\
that nearly every man experiences,\
and which holds him back more\
than any other,  is the\
inability to open his fucking mouth\
and say something&#8230;\
anything&#8230; to a\
girl he finds attractive. This\
is the Grand Hurdle,  the\
obstacle that looms like an unscalable\
wall between him and any new\
girl.</p>\
<p\
>Conquer this mental barrier,\
and you have improved your game\
a thousandfold from where you were\
before. Why do I say\
this?</p>\
<p\
>Because every time you don\
&#8217;t talk to\
a girl is a failure.\
A failure to at least give\
yourself a shot at sex and\
love with her. Think about\
that for a second. Each\
one of the thousands upon thousands\
of good-looking girls who\
have attracted your attention over the\
years that you didn&#8217\
;t talk to out of\
fear and apprehension is your failure\
.</p>\
<p>\
You have failed each and every\
one of those times,  and\
your instances of failure now add\
up to the thousands,  perhaps\
tens of thousands. Hundreds of\
thousands if you live in a\
non-obese oasis of America\
.</p>\
<p>\
That,  my friends,  is\
massive fail. No game technique\
can obliterate more failure,  more\
effectively,  than simply opening your\
mouth and saying something to the\
girl standing next to you.</\
p>\
<p>Let\
the words flow. You must\
abide the words.</p>\
\
<p>So powerful,\
and yet such a simple concept\
so universally rejected by the vast\
majority of men. See that\
cute girl in the aisle picking\
through the apples? You&#\
8217;re not the only\
man with lockjaw. Thousands of\
other men also stood stupefied as\
that same girl browsed apples all\
the other days of the year\
. Sure,  there were a\
couple of men here and there\
who managed to say something to\
her,  and now maybe one\
(or two) of those\
men are currently fucking her.\
But for the most part,\
your competition in the Just Say\
Something sweepstakes is laughably weak.</\
p>\
<p>So\
you shouldn&#8217;t\
worry about formulating the perfect witty\
opener,  or a great one\
-liner that will instantly attract\
her,  if that worry is\
causing you to abandon any attempt\
. You&#8217;re\
better off saying something geeky than\
saying nothing at all.</p\
>\
<p>Naturally,\
you will want to work at\
honing your JSS method so that\
what you do say is maximized\
toward piquing her interest. But\
if you&#8217;re\
tongue-tied,  mentally masturbating\
about the cleverness quotient of the\
opener you are mulling in your\
head is worse than staying silent\
. If the choice is between\
sullen silence and blurting out whatever\
nonsensical crap comes to you,\
always go with the nonsensical crap\
.</p>\
<p>\
In that spirit,  here are\
some JSS openers you can use\
in various scenarios. Some of\
these are cheesy,  and that\
&#8217;s the point\
. The goal is to get\
you talking in a natural,\
unforced way to a girl without\
dwelling too heavily on proper game\
technique.</p>\
<p\
>I know many of you\
men have stood in that supermarket\
line in front of the cute\
girl with your mouths glued shut\
,  hoping for a flash of\
inspiration which never came. Read\
these,  and be inspired to\
pull out your iPod earplugs.\
These are your first step to\
defeating the silence.</p>\
\
<p>Supermarket:</p\
>\
<p>&#8220;\
I hear frozen blueberries are in\
season this year.&#8221;</\
p>\
<p>&#8220\
;That&#8217;s\
an excellent ice cream choice.&#\
8221;</p>\
<p\
>&#8220;I&#8217\
;m going to read this\
tabloid and be proud of it\
.&#8221;</p>\
<\
p>&#8220;I sometimes\
judge people by their food purchases\
. Don&#8217;t\
say you&#8217;ve\
never done that.&#8221;</\
p>\
<p>Liquor\
store:</p>\
<p\
>&#8220;Do you think\
it&#8217;s possible\
to buy single cans of beer\
? I like to pretend I\
&#8217;m not a\
lush.&#8221;</p>\
\
<p>&#8220;That\
&#8217;s a good\
selection of bottom shelf liquor you\
got there.&#8221;</p\
>\
<p>&#8220;\
Where&#8217;s the\
beer funnel?&#8221;</p\
>\
<p>Book store\
:</p>\
<p>&#\
8220;Do you know where\
the pop-up/color\
by numbers book section is?&#\
8221;</p>\
<p\
>&#8220;I can&#\
8217;t believe this place\
doesn&#8217;t serve\
pizza.&#8221;</p>\
\
<p>Mall clothing store\
:</p>\
<p>&#\
8220;You ever notice how\
you always get more tired standing\
in a mall store than anywhere\
else?&#8221;</p>\
\
<p>&#8220;Is\
purple the new black?&#8221\
;</p>\
<p>&#\
8220;You look like the\
kind of girl who knows a\
lot about cufflinks.&#8221;</\
p>\
<p>Farmer\
&#8217;s market:</\
p>\
<p>&#8220\
;An apple always tastes better\
outdoors.&#8221;</p>\
\
<p>&#8220;I\
think my transformation to yuppie is\
complete.&#8221;</p>\
\
<p>&#8220;Did\
you try the fig butter?\
No? Count your blessings.&#\
8221;</p>\
<p\
>&#8220;The world would\
be a better place if we\
were all grass-fed.&#\
8221;</p>\
<p\
>Pool hall:</p>\
\
<p>&#8220;Don\
&#8217;t worry.\
That was just the stick.&#\
8221;</p>\
<p\
>&#8220;I drink until\
I see twelve holes. That\
&#8217;s how my\
game gets better.&#8221;</\
p>\
<p>Sidewalk\
,  waiting for crosswalk signal:</\
p>\
<p>Give\
her the stink-eye.\
&#8220;You look like\
the jay-walking type.&#\
8221;</p>\
<p\
>&#8220;Hi,  sidewalk\
stranger.&#8221;</p>\
\
<p>Porta-potty\
line:</p>\
<p\
>&#8220;Too late.\
I loaded my diapers.&#8221\
;</p>\
<p>\
Just kidding on that last one\
.</p>
'



gs4 = epub.EpubHtml(title='foot in the mouth',
file_name='foot_in_the_mouth.xhtml',
lang='en')
gs4.content='\
<h2>Game Is 50% Not Putting Foot In The Mouth</h2>\
<p> I was chatting up a\
    cute chick when I overheard\
    another pickup in progress right\
    next to me. The\
    guy was projecting his voice\
    loudly so I couldn&#\
    8217;t help but\
    hear just about every word\
    he said to the smiling\
    girl who was listening intently\
    to him. I glanced\
    over when I had a\
    moment to myself to observe\
    his success or failure.\
    (While watching other men\
     crash and burn is a\
     visceral pleasure,  I also\
     enjoy watching men succeed because\
     ,  one,  I can\
     always learn something new,\
     and,  two,  I\
     am still amazed how often\
     men in successful pickups utilize\
     game principles even when they\
     don&#8217;t\
     know they&#8217;\
     re doing that.)</p\
    >\
<p>The\
    guy was good-looking\
    and high energy. His\
    body language and voice tone\
    were confident. At one\
    point,  when he stepped\
    away to get a beer\
    ,  the girl&#8217\
    ;s friend leaned in\
and I heard her say &#\
8220;Wow,  he&#\
8217;s cute.&#8221\
; From my vantage,  at\
least until then,  this pickup\
was his to lose.</p\
>\
<p>Which he\
did. Back with beer in\
hand,  they continued talking,\
or rather,  he continued talking\
and punctuating his words with finger\
jabs into the air,  while\
she listened. And listened.\
And listened. Agonizing minutes ticked\
by. The energy was suddenly\
one-sided with his wild\
,  and panicky,  abandon,\
for he must have noticed her\
demeanor changing from delight to impassive\
politeness to confused annoyance. The\
previous pickup momentum,  torqued in\
large measure simply on the strength\
of his looks and initial pose\
of confidence,  dissipated with surprising\
rapidity as his &#8220;\
game&#8221; crumbled around\
him in a heap of monkey\
dancing,  gum flapping,  desperate\
body posturing,  and cloying oversmiling\
. He began leaning into her\
in a vain effort to compel\
her to commit to the waning\
conversation,  but she was already\
one foot out the door as\
her eyes darted around searching for\
a friend,  a lifeline,\
to pull her away from this\
once attractive man. His inner\
beta had betrayed him.</p\
>\
<p>Finally,\
denouement. A friend touched her\
elbow and whispered something in her\
ear. The guy figured out\
from her body language she was\
leaving soon,  so he suggested\
they exchange numbers. Or he\
might&#8217;ve suggested\
he give her his number,\
I couldn&#8217;t\
pick up what he said at\
that point very clearly. She\
took her phone out and he\
typed his number into it and\
gave it back to her.\
As she was leaving,  she\
didn&#8217;t look\
back at him. (A\
              good test whether a girl\
              will flake on you for\
              a future date is if\
              she looks back at you\
              briefly after you have gotten\
              her number and she is\
              leaving the premises with her\
              friends. No lookback =\
              flake.) But he wasn\
&#8217;t done yet\
. Still smiling like a tard\
getting tickled,  he shouted at\
her departing footsteps: &#8220\
;Hey,  you better memorize\
my number!&#8221;</p\
>\
<p>Woofa.</\
p>\
<p>It\
all went down in ten minutes\
. Let this be a lesson\
. Very good looks on a\
man without any game will buy\
him 30 seconds to ten minutes\
of an attractive girl&#8217\
;s attention,  after which\
he will be unceremoniously (and\
                            disappointedly) discarded just like\
any regular run of the mill\
schlub who doesn&#8217;\
t understand the art of seduction\
. Men need to stop projecting\
their fascination with looks onto women\
; personality and alphaness are what\
electrify a woman&#8217;\
s pleasure center. Good looks\
can send initial sparks,  (\
    and sparks is all it\
    is) but the allure\
wears quickly without compensatory game to\
buttress it.</p>\
<\
p>I number closed my\
girl. I did not tell\
her I would memorize her number\
.</p>\
'

gs5 = epub.EpubHtml(title='the sexual frame',
                file_name='the_sexual_frame.xhtml',
lang='en')
gs5.content='\
<h2>The Sexual Frame</h2>\
<p>One of the traits of the beta is\
that he is uncomfortable with animal\
sexuality &#8212; his own\
and especially that of the women\
he craves.  He is loathe\
to initiate contact,  late to\
respond to flirtatious signals,  and\
leery of acknowledging the raw sexual\
nature of women.  His unease\
with himself and with women&#\
8217;s equally ravenous sexual\
appetites compels him to constantly elevate\
women onto pedestals and to befriend\
them platonically before making his intentions\
known,  if ever.  He\
thinks that expressing his sexual nature\
too soon or too boldly will\
diminish them both.  He simply\
cannot conceive a scenario where a\
sexy girl will make love to\
him on the first day they\
meet.  This straightjacket of limiting\
beliefs is why he fails.</\
p>\
<p>A\
way to avoid these emotionally arid\
pitfalls is to adopt a frame\
of mind that is infused with\
sexuality.  Everything begins in the\
mind.  When I see an\
attractive girl across the room and\
start walking toward her I immediately\
picture her naked and writhing under\
my sheets,  sweating in ecstasy\
.  When I am talking with\
her and it is clear that\
we click,  I imagine what\
it would feel like to touch\
her bare skin.  I am\
kissing her before our lips have\
committed to the kiss.  As\
we delve deeper into conversation,\
a part of me visualizes peeling\
off her clothes and imagining transactions\
&#8230; scenarios&#8230\
; a dirty smutty world of\
possibilities.</p>\
<p\
>This is how every man\
should approach his interactions with women\
he is turned on by &#\
8212; unapologetically,  sensually,\
instinctually.  Civilized norms should hold\
no sway over your untamed thoughts\
or the id that fuels them\
.  They are yours to do\
with as you please and to\
set the tone of whatever follows\
.  The advantage to having this\
carnal mindset at all times lies\
in the power it gives you\
to draw women into your reality\
.  When a woman is into\
you she will sense your sexual\
energy and mirror it.  Your\
thoughts will become her thoughts.\
Your desire hers.  Later after\
sex when she is lying in\
your arms and talking about what\
led to this point you will\
discover that she knew it was\
going to happen when you knew\
.</p>\
<p>\
Lead as a man in making\
no excuses for your libertine nature\
,  and she will follow.</\
p>
'

gs6 =
epub.EpubHtml(title=' qualifying her',
file_name='qualifying_her.xhtml',
lang ='en')
gs6. content='\
<h2>Qualifying\
Her</h2>\
<p\
>What are two truisms of\
seduction?</p>\
<p\
>That women want to feel\
like they are valued for more\
than their looks.</p>\
\
<p>and</p\
>\
<p>That women\
want to earn a man&#\
8217;s interest.</p\
>\
<p>This is\
what the whole idea of qualifying\
women is based upon. By\
demonstrating to a woman that she\
must meet your standards which go\
beyond how she looks you indirectly\
communicate that</p>\
<\
p>a. you have\
discerning taste</p>\
<\
p>b. you are\
a challenge to be won</\
p>\
<p>c\
. you can be both a\
and b because you have choice\
in women.</p>\
<\
p>One way to demonstrate\
you have standards is by asking\
her questions designed to put her\
on the defensive. These are\
not open-ended &#8220\
;getting to know you&#\
8221; type questions like &#\
8220;what&#8217;\
s your favorite movie?&#8221\
;. They&#8217;re\
more incisive than that. The\
answer you want from her is\
implied in the question you ask\
,  so she&#8217;\
ll feel obligated to win your\
approval by answering the right way\
. Once the pickup ball starts\
rolling in this direction,  the\
power dynamic begins to shift away\
from her and to you.</\
p>\
<p>Following\
is a short list of effective\
qualifying questions that will let the\
girl know you are a choosy\
man. Timing is everything.\
Use them after you have gotten\
indications that she is attracted to\
you,  usually 10 to 15\
minutes after you&#8217;\
ve opened her if your game\
was tight. She will feel\
no reason to qualify herself to\
you if she isn&#8217\
;t already interested.</p\
>\
<ol>\
<li\
>Can you cook?</li\
>\
<li>Do you\
give good backrubs?</li>\
\
<li>Are you a\
good kisser?</li>\
<\
li>Do you do much\
traveling?</li>\
<li\
>Are you rich?</li\
>\
<li>Are you\
smart?</li>\
<li\
>Are you the jealous type\
?</li>\
<li>\
Is there more to you than\
just your looks?</li>\
\
<li>Are you low\
,  medium,  or high maintenance\
?</li>\
<li>\
Have you ever given a dollar\
to a homeless guy when no\
one else was watching?</li\
>\
</ol>\
<p\
>Don&#8217;t\
be afraid to express some disappointment\
if she doesn&#8217;\
t answer your question in a\
way that pleases you. Let\
the disappointment show on your face\
. Don&#8217;t\
make a huge production out of\
it; a deflated &#8220\
;oh,  i see&#\
8221; or &#8220;\
that&#8217;s too\
bad&#8221; will work\
just fine. If she quickly\
tries to correct the wrong impression\
she left with you then you\
&#8217;ll know she\
sees you as someone worthy of\
pleasing. She&#8217;\
ll be in chase mode,\
which is where girls WANT to\
be despite what they may claim\
to the contrary. (Older\
                  washed-up women,\
                  don&#8217;t\
                  bother contradicting what I say\
                  . You have forgotten what\
                  it&#8217;s\
                  like to be a young\
                  woman.)</p>\
<\
p>Qualification questions can also\
be framed in the form of\
statements. Saying any of the\
following in the course of a\
conversation,  sometimes with a half\
-serious grin to blunt the\
impact,  subtly projects that you\
are the one to impress,\
not the other way around.</\
p>\
<ol>\
<\
li>You better still look\
hot when you get older.</\
li>\
<li>I\
&#8217;m not interested\
in [XYZ].</li>\
\
<li>You get points\
for that.</li>\
<\
li>I&#8217;\
m gonna change the subject now\
.</li>\
<li>\
I don&#8217;t\
know if I can be with\
a girl who likes to [\
    XYZ].</li>\
</\
ol>\
<p>In\
my experience,  most men forget\
to qualify the girls they date\
. Their inner game is so\
geared toward trying to impress her\
that they never even think to\
turn the tables and interview HER\
for the job. When women\
go on dates,  they are\
interviewing the guys,  whether they\
admit this or not. The\
way to defeat her at her\
own game is not to accept\
her terms of engagement at all\
. Instead,  flip the script\
. Use her weapons of courtship\
against her. When she tries\
to qualify you,  brush off\
her attempts like you would dismiss\
a bratty little kid trying to\
goad you into a dare.\
The posture to adopt is amused\
mastery of everyone around you.</\
p>\
<p>After\
you&#8217;ve built\
up a store of experience with\
women,  you&#8217;\
ll start to have real standards\
that they must meet. Your\
choosiness will no longer be an\
artifact of game but a core\
component of who you are as\
a man. Having standards that\
include more than how she looks\
will make you very attractive to\
women,  because it subconsciously telegraphs\
that you are not so stricken\
by beauty like an inexperienced man\
that you would abandon your other\
criteria. When you can walk\
away from dates out of true\
conviction rather than tactical advantage your\
inner game will be like heart\
of lion.</p>\
'


gs7 = epub.EpubHtml(title='DQ Bluff',
 file_name='DQ_Bluff.xhtml',
lang='en')
gs7.content='\
<h2>What To Do If A Girl Calls Your Disqualification Bluff?<h2>\
<p>Disqualifications &#8212; false\
or genuine &#8212; are\
a powerful pickup tool. Pulling\
the rug out from under a\
girl who autonomically believes you desire\
her is a lickety-split\
way to raise your status vis\
a vis her status,  and\
thus delight her hypergamous reflex.\
The fact is,  women are\
constantly in a disqualification state of\
mind: she glides through the\
masses of maledom programmed to disqualify\
as many suitors as possible,\
and to settle upon the one\
man who is the best of\
all the men she can attract\
with her looks and youth.</\
p>\
<p>Knowing\
this,  the appropriation by the\
pickup artist of the female prerogative\
to disqualify is a classic example\
of flipping the seduction script and\
deviously moving the woman into the\
chaser role,  where she is\
more likely to perceive you as\
higher status and sexually desirable.\
Psych 101 and various books on\
influencing friends and clients touches upon\
this stuff,  but of course\
the estimable textbooks don&#8217\
;t follow the logic down\
the crimson road of poon hunting\
.</p>\
<p>\
There are four primary types of\
disqualification. Briefly,  I will\
describe them here,  before tackling\
the subject of this post&#\
8217;s title.</p\
>\
<p><strong>\
1. Preemptive self-disqualification\
</strong></p>\
<\
p>Introduced by Mystery,\
this is a statement you make\
to a girl that lets her\
know,  in so many words\
,  that you aren&#8217\
;t a serious prospect.\
You do this by disqualifying yourself\
. Examples: &#8220;\
I&#8217;m gay\
&#8221;,  &#8220;\
I&#8217;m in\
a relationship&#8221;,  &#\
8220;I&#8217;\
m not interested in dating at\
this point in my life&#\
8221;,  &#8220;I\
have the AIDS&#8221;,\
&#8220;I poop myself\
during scary scenes in movies&#\
8221;,  &#8220;I\
&#8217;m a male\
feminist&#8221;.</p>\
\
<p>This type of\
DQ (disqualification &#8212;\
    I don&#8217;\
    t feel like typing the\
    whole word out because my\
    pinky finger isn&#8217\
    ;t working,  fuck\
    you acronym haters) is\
called &#8220;preemptive&#\
8221; because it short circuits\
a girl&#8217;s\
hypergamous instinct by robbing her of\
the opportunity to disqualify you first\
. It essentially reverses the chaser\
-chased dynamic,  and upturns\
millions of years of evolutionarily molded\
female expectation. All of this\
works on the subconscious level.\
In the heat and fury of\
a real live social interaction,\
these game tactics fly under a\
girl&#8217;s conscious\
radar,  barely perceived by anyone\
but her omnipresent war room hamster\
and the hotline the fevered critter\
has to the gina general at\
the front.</p>\
<\
p>The preemptive self-\
DQ is intended to act as\
a bitch shield runaround: a\
girl is less likely to blow\
you out if you make her\
think you&#8217;re\
not available to her in the\
first place.</p>\
<\
p><strong>2.\
Target disqualification</strong></p\
>\
<p>Self-\
explanatory,  this is a tactic\
whereby the man disqualifies the girl\
from being a serious mating prospect\
. Owing to the greater chance\
that Target DQ can be perceived\
by the woman as sour grapes\
,  this is a more aggressive\
,  and thus riskier,  form\
of DQ,  its risk weighed\
against a potentially more rewarding payoff\
. Examples: &#8220;\
You seem like you&#8217\
;d make a great friend\
&#8221;,  &#8220;\
You&#8217;re not\
really my type&#8221;,\
&#8220;You&#8217\
;re a good girl,\
I&#8217;m nothing\
but trouble&#8230; we\
would never work&#8221;,\
&#8220;I&#8217\
;m glad you&#8217\
;re off the market&#\
8221; [just assume she\
       &#8217;s off\
       the market],  &#8220\
;Phew,  so nice to\
talk to a girl who isn\
&#8217;t trying to\
flirt with me&#8221;,\
&#8220;Since your vagina\
is cemented shut by a rare\
disease,  I can talk to\
you like you&#8217;\
re one of the guys&#\
8221;,  &#8220;You\
&#8217;re the first\
lesbian I&#8217;ve\
met in this town&#8221\
;.</p>\
<p>\
The Target DQ is less about\
lowering a woman&#8217;\
s bitch shield than it is\
about instigating a woman to qualify\
<em>herself</em\
> to <em>you\
</em>. It&#8217\
;s a more proactive DQ\
compared to the PSDQ above,\
serving as it does as an\
immediate status differential cue to the\
woman that she has to do\
something to correct the imbalance to\
the natural order of things.\
This &#8220;something&#\
8221; usually involves convincing you\
,  the incorrigible player,  that\
she is hot and sexy and\
goodtogo. PSDQs are female disqualification\
&#8212; aka rejection &#\
8212; avoiders or neutralizers,\
while TDQs are meant to coax\
women into self-qualifying.</\
p>\
<p><strong\
>3. Handicap Principle self\
-disqualification</strong></p\
>\
<p>This is\
a sub-genre of <\
a href="https://heartiste\
.wordpress.com/2009\
/01/29/vulnerability\
-game/" target="_blank\
">vulnerability game</a>,\
and promoted by Charisma Arts (\
    A Wayne Elise aka Juggler\
    production). Basically,  you\
bring up some faux embarrassing thing\
about yourself &#8212; some\
minor personality flaw that you blow\
up into significance &#8212;\
and reveal it to the girl\
. The theory behind the Handicap\
Principle is that women perceive men\
who are comfortable &#8220;\
handicapping&#8221; themselves &#\
8212; either through bright plumage\
(peacocking) or through admission\
of beta characteristics &#8212;\
as alpha males,  because who\
else but an alpha male would\
be strong and powerful enough to\
shoulder a weak beta flaw without\
suffering any hit to his overall\
status?</p>\
<p\
>Be careful with the Handicap\
Principle. First,  it&#\
8217;s a theory,\
an elegant one to be sure\
,  but one that remains,\
as far as I know,\
largely unproven by evolutionary biologists.\
The degree to which HP might\
apply to humans is unknown.\
At some great enough level of\
flaw possession,  the Handicap Principle\
must surely break down,  and\
we see evidence for this in\
the many stories of alpha males\
<a href="https://\
heartiste.wordpress.com/\
2011/01/18/\
beta-valentine/" target="\
_blank">who became beta in\
relationships</a> and then\
lost their women&#8217;\
s love. Personally,  I\
think the Handicap Principle is easily\
confused with the theory of sexual\
selection,  but that is a\
topic for a future post.</\
p>\
<p>Nonetheless\
,  it is true that women\
coo for the alpha male who\
unloads a perfectly timed admission of\
(cute) self-abnegation\
. Examples: &#8220;\
Oh man,  I&#8217\
;m so bad at figuring\
out if women are flirting with\
me or not&#8221;,\
&#8220;I don&#\
8217;t dance,  I\
&#8217;ve got two\
left feet&#8221;,  &#\
8220;Ever since an unfortunate\
childhood trauma,  I&#8217\
;ve had a fear of\
puppies&#8221;,  &#8220\
;Black people scare me&#\
8221;.</p>\
<p\
>The trick is to admit\
your &#8220;flaws&#\
8221; with utmost confidence and\
unconcern. Don&#8217;\
t say them as if you\
&#8217;re waiting to\
judge her reaction. They should\
be spoken off-the-\
cuff,  almost as if you\
&#8217;re unaware that\
there is a girl standing there\
listening to you. NEVER admit\
to a real beta flaw that\
would repulse most women; i\
.e. &#8220;\
I go limp when a woman\
makes more money than I do\
&#8221;.</p>\
<\
p><strong>4.\
Beta bait disqualification</strong></\
p>\
<p>Another\
Juggler specialty,  the idea behind\
the BBDQ is to disqualify yourself\
as a sucker for women&#\
8217;s flirtations. This\
is a minor school of DQ\
that you probably won&#8217\
;t use or need very\
often,  but when you do use it,  its power is undeniable. Women\
will very frequently try to &#8220;tease out&#8221; beta males\
by complimenting men and judging them on their reactions.\
Does the man express a\
little too much appreciation for her compliment? BETA.\
Does he seize upon her\
compliment as a springboard to ask her out? BETA. Does he say &#\
8220;Wow,  no girl has ever said something so kind to me before\
!&#8221;? BETA.</p>\
<p>But if a woman compliments\
you,  and your reaction is to ignore it,  downplay it,  or even\
disagree with her (without veering into self-deprecation territory),\
she will think\
ALPHA. Examples: &#8220;Thanks,  but this actually isn&#8217\
;t my favorite shirt&#8221;,  &#8220;You like these shoes\
? You&#8217;re easy to please&#8221;,  &#8220;\
Yes,  that bulge is my penis. Now you&#8217;ve made\
me self-conscious&#8221;.</p>\
<p>The BBDQ is\
both a self-disqualification and a target disqualification.\
You deny the woman&#\
8217;s positive assessment of you,  while simultaneously denying\
her power over your\
emotions. It is a very subtle art form that,  when mastered,  is\
chick crack to women&#8217;s status discernment modules. A successful BBDQ\
is only superficially a signal of modesty; underneath the\
calculated modesty is a heat\
-seeking missile aimed straight at a woman&#8217;s id heart that\
explodes in a fireball of lust for your total lack of interest in winning her\
approval.</p>\
<p>***</p>\
<p>DQs are one\
of the most difficult game techniques for noobs to grasp.\
They are tangentially related\
to negs,  and like the neg,  they are often abused and misused by\
beginners. Their power is also their danger; because they work so well,\
men new to the game have a tendency to throw them out at awkward moments\
,  and with too much expectant fervor. They then come across as creeps and\
try-hards,  and wind up providing fodder to bitches to later log into\
the social media borg to mock the hapless betas who tried to run game on\
them.</p>\
<p>(Leave it to a woman to mock a\
    man for trying. You don&#8217;t hear too many men\
    mocking fat chicks who make a real effort to lose weight by going to\
    the gym and eating right. But then,  in some respects,  men\
    simply have more compassion and empathy than do women\
    for the opposite sex.\
    But I ingest.)</p>\
<p>The keys to getting your\
DQ money&#8217;s worth are timing,  context and delivery. Too\
soon &#8211;&gt; weird. Too late &#8211;&gt;\
spiteful. Too unrelated &#8212; &gt; try-hard. Too\
forced &#8211;&gt; creepy. Too self-deprecating &#8211;&\
gt; beta. Too nasty &#8211;&gt; sour grapes.</p\
>\
<p>But even when you have timing,  context and delivery down\
pat,  you will sometimes get your DQ called out by a woman.</p\
>\
<p>You: &#8220;I&#8217;m not\
looking for anyone right now.&#8221;</p>\
<p>Girl:\
    &#8220;Good,  because neither am I.&#8221;</p>\
\
<p>***</p>\
<p>You: &#8220;You&#\
8217;re a good girl,  I&#8217;m trouble&#8230\
; we would never work out.&#8221;</p>\
<p>Girl\
: &#8220;Yeah,  I guess I am a good girl.&#8221\
;</p>\
<p>***</p>\
<p>You: &#8220\
;I&#8217;ve got a weird fear of puppies. Goes back\
to a childhood incident.&#8221;</p>\
<p>Girl: &#\
8220;That&#8217;s fucked up.&#8221;</p>\
<\
p>***</p>\
<p>You: &#8220;Thanks,  but\
this isn&#8217;t my favorite shirt.&#8221;</p>\
<\
p>Girl: &#8220;Yeah,  now that I look at it\
closely,  it&#8217;s not a very good shirt.&#8221;</\
p>\
<p>Don&#8217;t worry. These kinds of\
reactions,  as plausible as they\
are in writing,  and as\
much as cunts\
will cackle that\
they will respond like this to\
players whenever one of them tries\
\
to hit on their skanky carcasses\
,  are blessedly rare. Most\
girls will be\
too high on\
their torqued emotions to call out\
a player&#8217;s\
\
DQ bluff so directly. The\
hamster is simply not that rational\
; hence,\
why he&#\
8217;s called the rationalization\
hamster,  devoted to creating rationale\
\
out of nothing at all.</\
p>\
<p>But\
DQ bluff-\
calling does happen\
,  and more often to newbs\
than to experienced PUAs. When\
\
a newb gets his DQ bluff\
called,  the result can be\
hilarity (not\
            to mention the\
        newb&#8217;s\
          demanding his money back from\
          some\ overpriced pickup seminar he\
          attended). A great illustration\
of a newb&#8217\
;\
s DQ bluff being called out\
was provided by Juggler in <\
a href\
="https://heartiste\
.wordpress.com/2012\
/07/09/\
wayne\
-elise-pacing-and\
-conversational-context/" target\
="_blank\
">this post</\
a>.</p>\
<blockquote\
><p>ASPIRING NOOB\
:\
    “I could. But\
    I’m not going\
    to. I’\
m\
an all out there kinda guy\
. I’m going to\
this fab\
party later. If\
you’re lucky I might\
invite you.”</p>\
\
\
<p>GIRL: “\
No thanks.”</p>\
<\
p>“Aww\
. You’\
re playing hard to get.\
That’s so cute.”</\
\
p>\
<p>“Whatever\
.”</p>\
<p>“\
I hear an\
accent. Where\
are you from?”</p>\
\
<p>“Nowhere.”</p\
>\
<p>“Ha.\
Nowhere. That’s funny\
. Can I\
buy you a\
drink?”</p>\
<p\
>“Yes. I’ll\
\
take a piña colada but don\
’t even think about dropping\
a roofie in\
there. I\
’m not going to hook\
up with you.”</p>\
\
\
<p>“Whoever said\
anything about hooking up? You\
’re more of\
the kinda\
girl I see as a friend\
.”</p>\
<p>“\
Good\
.”</p>\
<p\
>“Good. So what’\
s your name?”</\
p></\
blockquote>\
<p>If\
a girl isn&#8217;\
t\
already invested in the conversation\
with you,  a DQ is\
less likely to have\
the intended\
effect. If you walk up\
to a girl cold and start\
spouting\
off about how you just\
want to be friends with her\
and you aren&#\
8217;\
t available for dating,  what\
kind of reaction do you think\
you\
&#8217;ll get\
? Do you imagine girls will\
start qualifying themselves to\
you on\
the spot? No,  you\
have to first reel her in\
and\
dangle the promise of your\
interest before unloading the soul-\
sucking DQ.</p\
>\
<\
p>Many PUAs,  like\
Tyler Durden,  recommend a preemptive\
approach\
to DQing; that is\
,  you train yourself to sense\
when girls are about\
to disqualify\
you,  and disqualify them before\
they get a chance. Often\
,\
this occurs during the late\
comfort stage of the seduction,\
when the girl is\
beginning to\
feel pangs of guilt about the\
release of her inner slut which\
looms\
on the horizon. Other\
PUAs,  like Mystery,  advocate\
active DQs early in the attraction\
phase,  as a direct method\
for building attraction. Still others\
say to avoid them entirely,\
as the risk of delving into\
&#8220;sour grapism&#\
8221; territory is too great\
to assume.</p>\
<\
p>I will say this\
about DQs:</p>\
<\
p>They are supposed to\
sound spontaneous. The best DQs\
are unexpected and off-the\
-cuff. If it sounds\
like a line,  it will\
backfire. If it sounds like\
you thought about it beforehand,\
it will backfire. Body language\
and facial expression are important conveyors\
of indifference and spontaneity.</p\
>\
<p>Never DQ\
from a position of weakness.\
If you are working overtime to\
keep a girl&#8217;\
s attention,  a DQ will\
only lower your value even more\
. Remember,  DQs are FALSE\
disqualifications. When you DQ as\
a last resort to keep a\
girl around,  it is no\
longer false; it is a\
real disqualification.</p>\
<\
p>If a girl calls\
out your DQ,  my best\
advice is to ignore it and\
change the subject,  OR readily\
agree with her in return.\
A pinpoint DQ destroyer,  while\
rare,  is not to be\
trifled with. You want to\
avoid at all costs the impression\
of being flustered or annoyed or\
dispirited by her agreement with your\
DQ. Just roll with it\
,  as if you&#8217\
;re glad she agreed with\
you,  and reassess if she\
&#8217;s worth your\
continued effort to bed.</p\
>\
<p>The upside\
to a failed DQ is that\
,  later,  if the girl\
is into you and starts to\
return your interest,  you can\
remind her of the claim she\
made earlier about not wanting this\
to go anywhere. A pullback\
at a moment when the girl\
MOST WANTS TO PULL INTO YOU\
is like sticking TNT up her\
hamster&#8217;s anus\
. You are beginning down the\
road of building your own slave\
harem.</p>\
<p\
>Preemptive DQs &#8212;\
the type of DQ that occurs\
before you have built adequate interest\
in the girl (think Mystery\
             Method-style) &#\
8212; can work great IF\
you don&#8217;t\
linger on them waiting for a\
reaction. You drop the DQ\
,  ignore whatever reply she gives\
in return,  and plow.\
The goal is subconscious infiltration,\
leading to script flipping.</p\
>\
<p>Mystery-\
style preemptive DQs work best on\
hot girls. Since hot girls\
are the most likely to assume\
every man wants them (justifiably\
                      ),  a quick correction to\
the contrary can temporarily scramble their\
status differential discernment algorithms.</p\
>\
<p>Be careful\
about DQing 6s and 7s.\
You can easily blow a girl\
out of the water and render\
yourself unattainable to them.</p\
>\
<p>If you\
&#8217;re going to\
agree with a girl&#8217\
;s DQ nuke,  don\
&#8217;t make a\
production out of it. For\
example:</p>\
<p\
><span style="text-\
decoration:underline;">WRONG WAY\
TO AGREE WITH GIRL&#8217\
;S DQ NUKE</span\
></p>\
<p>\
Girl: &#8220;Good\
. I just want to be\
friends too.&#8221;</p\
>\
<p>You:\
    &#8220;Yeah,\
    yeah,  friends. That\
    &#8217;s what\
    I want to.&#8221\
    ; [pained expression belies\
       your words]</p>\
\
<p><span style="\
text-decoration:underline;">\
RIGHT WAY TO AGREE WITH GIRL\
&#8217;S DQ NUKE\
</span></p>\
<\
p>Girl: &#8220\
;Good. I just want\
to be friends too.&#8221\
;</p>\
<p>\
You: &#8220;Cool\
. So&#8230; you\
see that guy over there?\
I think he wants you.\
That&#8217;s the\
way to do it. Stare\
hard.&#8221;</p>\
\
<p>In Juggler&#\
8217;s example above,\
when the NOOB says &#8220\
;If you&#8217;\
re lucky I might invite you\
&#8221;,  he&#8217\
;s expecting the girl to\
reply something along the lines of\
&#8220;Wow,  you\
must think you&#8217;\
re special&#8221;,  a\
shit test to which the NOOB\
thinks he is well-trained\
to parry. But instead,\
she deflates him totally with the\
cold &#8220;No thanks\
&#8221;. The NOOB is\
now left flailing,  hurling more\
DQs at her in hopes one\
will stick.</p>\
<\
p>The best defense against\
the deflating DQ nuke is to\
simply avoid putting yourself in the\
position where such nukes are likely\
to happen. If you pace\
yourself,  the likelihood of triggering\
a DQ nuke goes way down\
. Should one happen to you\
,  one that is particularly disheartening\
,  you may consider bailing.</\
p>\
<p>You\
: &#8220;If you\
&#8217;re lucky I\
might invite you.&#8221;</\
p>\
<p>Girl\
: &#8220;No thanks\
.&#8221;</p>\
<\
p>You: &#8220\
;Ok. See ya.&#\
8221;</p>\
<p\
>A good player knows when\
to cut his losses.</p\
>\
<p>However,\
if you see an opening and\
want to continue working on her\
,  <strong>AGREE AND\
REDIRECT</strong>.</p>\
\
<p>You: &#\
8220;If you&#8217\
;re lucky I might invite\
you.&#8221;</p>\
\
<p>Girl: &#\
8220;No thanks.&#8221\
;</p>\
<p>\
You: &#8220;Yeah\
,  come to think of it\
,  it&#8217;s\
probably better you don&#8217\
;t come. My ex\
might start a fight with you\
.&#8221;</p>\
<\
p>OR</p>\
\
<p>You: &#\
8220;Well,  I suppose\
now I can make room for my Mom to come with me.&#8221;</p>\
<p>OR</p>\
<p>You: [fake look of indignation] &#8220;Invite&#8230; REVOKED.&#8221;</p>\
<p>OR</p>\
<p>You: &#8220;Great,  now who am I gonna set up my friend with?&#8221;</p>\
<p>OR</p>\
<p>You: &#\
8220;Damn,  I guess\
I&#8217;ll have\
to buy my own drinks.&#\
8221;</p>\
<p\
>This has been an introductory\
course in DQs and sidestepping DQ\
nukes. The subject material is\
advanced,  so I encourage the\
commenters to flesh it out for\
the 1 billion readers who are hanging on your every word.</p>
'

gs8 = epub.EpubHtml(title='a-hole game part i',
 file_name='a-hole_game_part_i.xhtml',
lang='en')
gs8.content='\
<h2>A-Hole Game Part I</h2>\
s week I will discuss Asshole\
Game. There is no sugarcoating\
it; being an asshole works\
on women,  all women,\
most of the time. Any\
man who has lived a day\
in his life and isn&#\
8217;t self-deluded\
by equalist ideology or chick flic\
romanticism knows this is true,\
even those PUA &#8220;\
love gurus&#8221; who\
unctuously sermonize that what women really\
want are &#8220;strong\
confident men&#8221; minus\
the asshole part. Save your\
holier-than-thou moralizing\
and desperate attempts to discredit asshole\
game by falsely claiming it only\
appeals to low self esteem girls\
. We&#8217;re\
going to discuss what works,\
not what <em>should\
</em> work.</p\
>\
<p>I&#\
8217;ve written before about\
how effective <a href="\
https://heartiste.wordpress.\
com/2008/03/\
21/when-a-\
girl-needs-an-\
asshole/" target="_blank">\
asshole game</a> is\
at attracting and <a href\
="https://heartiste.wordpress\
.com/2008/04\
/15/keeping-your\
-woman-in-line\
/" target="_blank">keeping\
your women in line</a\
>. If you&#8217;\
ve been in a rut,\
or you&#8217;re\
having troubles with your girlfriend (\
    almost always instigated by the\
    girl),  acting like an\
asshole is the quickest and most\
efficient way to set things straight\
. I was talking about this\
with a couple friends recently and\
they agreed that no matter how\
often they see asshole game work\
,  they still can&#8217\
;t accept the reality of\
it. I hear this said\
all the time from friends who\
have witnessed me using asshole game\
on a girl: &#8220\
;I can&#8217;\
t believe that works.&#8221\
; No surprise. No man\
truly wants to believe that soul\
of a woman was created below\
.</p>\
<p>\
I&#8217;m going\
to briefly describe a scenario from\
my own life when I was\
an asshole with a girl,\
and what effect it had on\
her. Use my lessons in\
your own life and be amazed\
at the results it gets you\
. (No,  seriously.)\
In the comments,  feel free\
to offer your own asshole suggestions\
for how you would have handled\
the situation I present.</p\
>\
<p>I was\
six months into a relationship with\
a pretty au pair (standard\
                  MO: ten years younger\
                  ). She lived outside the\
city. I was already telling\
her to &#8220;see\
me on a Tuesday night,\
because this weekend is tough for\
me. And you need to\
research getting your green card.&#\
8221; I said this because\
secretly I was in hunter mode\
and wanted the weekend nights to\
myself for preying on fresh meat\
. My friends thought I was\
crazy. &#8220;She\
&#8217;s the perfect\
girlfriend. Why would you fuck\
that up?&#8221; &#\
8220;She&#8217;\
s going to know you&#\
8217;re out at the\
clubs hitting on girls. She\
&#8217;ll leave you\
.&#8221; That&#8217\
;s all I ever heard\
from them.</p>\
<\
p>One of those weekend\
nights I was at a music\
club with friends,  chatting with\
some goth chicks standing around us\
. Late in the night,\
my au pair girlfriend showed up\
at the club,  unexpectedly.\
She had had her host family\
drop her off in front of\
the club at 1 am.\
I never told her where I\
would be at,  let alone\
that I was even going out\
that night. She simply guessed\
and nailed it. I didn\
&#8217;t see her\
come in. My friends looked\
over my shoulder with raised eyebrows\
as my GF sidled up behind\
me and put her arms around\
my waist.</p>\
<\
p>*ASSHOLE ALERT*</p\
>\
<p>I turned\
around and looked at her without\
smiling,  the disappointment etched onto\
my face. I remember the\
thoughts going through my head:\
    &#8220;Oh man\
    ,  I won&#8217\
    ;t be able to\
    hit on any girls now\
    that she&#8217;\
    s here.&#8221;\
    I muttered &#8220;\
    Hey&#8221; and\
    with a hint of annoyance\
    asked her how she got\
    there. I told her\
    to get herself a drink\
    . She never left my\
    side for the rest of\
    the night while I constantly\
    glanced around the room.\
    Her eyes blazed with a\
    mixture of love and worry\
    .</p>\
<p>We stayed together for another year. It went\
on like this for a while\
: Me keeping a distance to\
surreptitiously hit on new women,\
her chasing after me. The\
sex never faltered. It was\
always hot and her pussy dripped\
like a faucet right up until\
the end.</p>\
<\
p>There are genuine assholes\
who are loved,  and there\
are spiteful assholes who get nowhere\
. The difference is crucial.</\
p>\
<p>Uncaring\
asshole = success with women.</\
p>\
<p>Caring\
asshole = failure with women.</\
p>\
<p>When\
women say they don&#8217\
;t fall for assholes,\
they are thinking of the second\
kind. A caring asshole comes\
from a place of bitterness and\
spite. His assholery is reactive\
rather than proactive. He is\
poor at calibrating which women will\
be responsive to his dick attitude\
. Caring assholes are crassly insulting\
and transparently invested in the outcome\
of their game.</p>\
\
<p>Uncaring assholes are\
assholes as a consequence of their\
indifference. It is the aloofness\
of the man she loves that\
drives women crazy with obsession*,\
and that aloofness is manifest as\
asshole behavior. An uncaring asshole\
demonstrates clearly in his body language\
and tone of voice,  not\
to mention his dearth of words\
,  that he could take her\
or leave her. In the\
scenario above,  my asshole behavior\
mirrored my feelings perfectly &#8212\
; I really did not want\
her there by my side that\
night.</p>\
<p\
>*Why do women love assholes\
? Quickie answer: Sexy Sons\
hypothesis.</p>
'


gs9 = epub.EpubHtml(title='a-hole game part ii',
 file_name='a-hole_game_part_ii.xhtml',
lang='en')
gs9.content='\
<h2>A-Hole Game Part II</h2>\
<p><span style="text-decoration:underline;">\
Asshole game with 25 year old \
foreign girlfriend</span></p\
>\
<p>Her: \
    I love Indian culture. \
    The dancing,  the colorful \
    dresses,  the religion&#\
    8230;</p>\
<\
p>Me: You love \
Bollywood? There&#8217;\
s no accounting for taste.</\
p>\
<p>Her\
: [getting seriously agitated] \
Shut up! The Indian culture \
is beautiful.</p>\
<\
p>Me: Hey,  \
there&#8217;s an \
Indian guy who lives down the \
street. Go knock yourself out\
. You can get some of \
his culture long and hard.</\
p>\
<p>Her\
: You&#8217;re \
an ignorant American. A child\
. What do you know.</\
p>\
<p>Me\
: I know you&#8217\
;re being annoying.</p\
>\
<p>Later &#\
8212; pussy dripping sex.</\
p>\
<p><span \
style="text-decoration:\
    underline;">Asshole game with \
    bartender chick</span></\
    p>\
<p>\
Me: [looking at her \
     new hairstyle with a grimace\
     ] What did you do \
to your hair!?</p>\
\
<p>Her: I \
got bangs! Jesus,  fuck \
you.</p>\
<p\
>Me: It doesn&#\
8217;t work for me\
.</p>\
<p>\
Three months later &#8212; \
pussy dripping sex. And free \
drinks.</p>\
<p\
><span style="text-\
decoration:underline;">Asshole game \
with heavily tattooed chick in indie \
club</span></p>\
\
<p>Me: Hi\
.</p>\
<p>\
Her: [sighing] Just \
to let you know up front\
,  I&#8217;m \
not interested.</p>\
<\
p>Me: So you\
&#8217;re not going \
to introduce me to your cute \
friend?</p>\
<p\
>Later &#8212; no \
sex,  but pride as a \
man.</p>\
<p\
><span style="text-\
decoration:underline;">Asshole game \
with girl trying to break up \
with me in Starbucks</span\
></p>\
<p>\
Her: I really think this \
isn&#8217;t going \
to work. I don&#\
8217;t want to do \
this anymore. Look at us\
.</p>\
<p>\
Me: [slouching for maximum \
     aloofness effect] I can \
read your face. You&#\
8217;re a bad liar\
. But if this is what \
you want then go ahead. \
I gotta admit you&#8217\
;re not easy to be \
in a relationship with. You\
&#8217;re a fucking \
pain in the ass.</p\
>\
<p>Her: \
    What&#8217;s \
    that supposed to mean?!?</\
    p>\
<p>Later &#8212; six more \
months of pussy dripping sex.</\
p>\
<p>***</p\
>\
<p>Note: \
    Never smile when running asshole \
    game. It&#8217\
    ;ll look like you\
    &#8217;re backpedaling\
    .</p>
'


gs10 = epub.EpubHtml(title='a-hole game part iii',
 file_name='a-hole_game_part_iii.xhtml',
lang='en')
gs9.content='\
<h2>A-Hole Game Part III</h2>\
<p><em>Previously\
: <a href="https\
://heartiste.wordpress.com\
/2009/01/12\
/a-hole-game\
-day-1/" target\
="_blank">Asshole Game: \
    Day 1</a> \
    and <a href="\
    https://heartiste.wordpress\
    .com/2009/\
    01/13/a\
    -hole-game-\
    day-2/" target\
    ="_blank">Asshole Game\
    : Day 2</a\
    ></em></p>\
\
<p>Uncaring asshole game \
will revitalize a flagging relationship and \
help keep the love strong.</\
p>\
<p>One \
weeknight around 1 AM I got \
a frantic call from my girlfriend\
. She wailed that she had \
gotten into an accident and needed \
help. Looking over at my \
clock and realizing it was six \
hours until I had to get \
up for work,  I sighed \
heavily and asked her if the \
accident was serious. She cried\
. <em>&#8220;\
Whaat?? I don&#8217\
;t know,  yes it\
&#8217;s serious! \
I don&#8217;t \
know what to do!&#8221\
;</em> I told her \
to calm down and explain what \
happened. Between her sobs I \
could piece together the events. \
She had driven back from a \
job and was parallel parking on \
a street in her neighborhood close \
to her home,  which was \
about a twenty minute walk from \
my place. In the process \
of parking,  she had hit \
the SUV in front of her\
. Her car,  presumably,  \
was sticking out into the street \
a bit.</p>\
<\
p>A parallel parking &#\
8220;accident&#8221;? \
There was no way I was \
rousing myself from my comfortable slumber \
and traipsing out there in the \
middle of the night to console \
her for a minor fender bump\
. How bad can a girl \
fuck up parallel parking? I \
thought for a second. My \
girlfriend was a skittish,  uncoordinated \
driver. Stereotypically female behind the \
wheel. Yeah,  if anyone \
could turn a parallel park job \
into a five car pileup it \
would be her. Then I \
thought about where she was parked\
. Her neighborhood was sketchy (\
    i.e not enough \
    SWPLs had moved in yet\
). If I were a girl\
,  I wouldn&#8217;\
t walk around there at 1 \
AM. I thought some more\
.</p>\
<p>&#\
8220;Look,  just leave \
your car there and go home\
. It&#8217;s \
late. Get some sleep. \
I have to work tomorrow. \
We&#8217;ll check \
out your car in the morning\
. Whatever happened,  it can\
&#8217;t be that \
bad,  so stop freaking out \
about it. You just bumped \
a fender.&#8221;</p\
>\
<p><em>&#\
8220;I can&#8217\
;t just leave it!&#\
8221;</em> She was \
really crying now. <em\
>&#8220;You have to \
come! Please,  take a \
look. It&#8217;\
s bad. I don&#\
8217;t like standing out \
here. It&#8217;\
s dark and there are weirdos \
walking around. Just help me\
!&#8221;</em></p\
>\
<p>Fucking Christ\
. &#8220;Don&#\
8217;t make a big \
fucking production out of this! \
You bumped your car,  it\
&#8217;s not a \
huge deal to get worked up \
over. Calm down and just \
walk home. I&#8217\
;ll be there in the \
morning.&#8221;</p>\
\
<p><em>&#8220\
;Please come,  pleeeeeease!!!&#\
8221;</em></p>\
\
<p>Annoyed that my \
sleep was interrupted,  and irritated \
with my girlfriend for spazzing out \
over nothing,  I drove to \
the scene of the tardishness. \
She was pacing next to her \
car,  arms crossed,  tears \
running down her face. I \
examined the car. Holy shit\
. There was a giant gouge \
in the right front panel where \
she had turned the car too \
early as she was backing up \
into the empty parking spot. \
I couldn&#8217;t \
believe someone could cause that much \
damage from parallel parking,  not \
even a hysterical girl.</p\
>\
<p>&#8220;\
What the hell did you do\
?!&#8221;</p>\
<\
p>She explained that once \
her car bumped into the SUV \
up front,  instead of doing \
the logical thing and pulling out \
to try again,  she had \
freaked out and kept her foot \
on the gas pedal,  trying \
to force her tiny Toyota into \
the spot. Result: A \
deep resale value-killing indentation \
from her car grinding into the \
bumper of the SUV. I \
get exasperated with stupidity,  so \
I gave her the cold,  \
hard stare of contempt.</p\
>\
<p>&#8220;\
Give me the keys.&#8221\
;</p>\
<p>\
I pulled her car forward and \
parked it in the empty spot \
without incident.</p>\
<\
p><em>&#8220;\
I wanted you to come help\
. I was scared out here\
.&#8221;</em></p\
>\
<p>I pointed \
at her house across the street\
. &#8220;You could\
&#8217;ve pulled your \
car out and parked like a \
normal human being,  and then \
gone home instead of dragging me \
out here for nothing. Don\
&#8217;t play these \
little drama acts with me.&#\
8221;</p>\
<p\
>She looked down at the \
ground. The streetlight reflected off \
her tear streaked face. <\
em>&#8220;What will \
we do about the car now\
?&#8221;</em></p\
>\
<p>&#8220;\
I don&#8217;t \
know. We&#8217;\
ll talk about it tomorrow.&#\
8221; I didn&#8217\
;t offer her to come \
back to my place. &#\
8220;Try not to think \
about it and go to sleep\
.&#8221;</p>\
<\
p>The next evening she \
was at my place,  apologetic \
but also hurt that I didn\
&#8217;t rush to \
her side like a white knight\
. I barely paid her feelings \
any heed. Her pain simply \
didn&#8217;t register\
. That night,  we watched \
porn and I did her in \
the ass for the first time\
. She welcomed my meaty intrusion\
.</p>\
<p>\
When I told a good friend \
what had happened,  the words \
he used to describe me were \
&#8220;Grade A schmuck\
. Complete asshole.&#8221; \
Then he wondered why she was \
still with me and said I \
didn&#8217;t deserve \
her.</p>\
<p\
>She and I stayed together \
for another year. The sex \
was always available and her pussy \
moist. She never had a \
&#8220;headache&#8221\
;. She accepted my facials with \
clocklike regularity. In hindsight,  \
she fit the description of a \
Neurotic Waif perfectly,  with elements of the Eternal Ingenue.</p>\
<p>The best Asshole \
Game is when the assholery comes \
naturally and effortlessly. What I \
did was not good by most \
people&#8217;s definition \
of the good,  but there\
&#8217;s no denying \
it worked. After that incident\
,  she was in love with \
me more than ever.</p >
'


gs11 = epub.EpubHtml(title='being the right kind of asshole',
 file_name='being_the_right_kind_of_asshole.xhtml',
lang='en')
gs11.content='\
<h2>Being The Right Kind Of Asshole</h2>\
<p>Occasionally,  an \
oh-so-sincere skeptical \
reader will insist that being the \
jerk women love doesn&#8217\
;t work,  because he\
/she/it saw some \
guy calling a girl a bitch \
once,  and that guy didn\
&#8217;t get laid\
.</p>\
<p>\
The height of counter-argument \
prowess!</p>\
<p\
>As this blogasmic beacon of \
bounteous love has <a href\
="https://heartiste.wordpress\
.com/2011/12\
/22/caring-vs\
-uncaring-assholery/" target\
="_blank">written before</\
a>,  there is a critical \
distinction between being a &#8220\
;caring asshole&#8221; \
that signals to women you are \
desperate for their vaginas,  and \
being an aloof &#8220;\
uncaring asshole&#8221; that \
signals to women you could do \
without their vaginas,  which ironically \
makes their vaginas feel strong love\
.</p>\
<p>(\
    I will leave aside for \
    another post examination of putative \
    examples to the contrary,  \
    such as those supreme assholes \
    like Chris Brown and Mexican \
    drug lords who,  full \
    of care,  beat their \
    women to pulps yet still \
    enjoy the undying love of \
    their attractive targets of affliction\
    .)</p>\
<p\
>If you are having trouble \
dissecting the meaning of being an \
uncaring asshole,  think upon the \
personality quirks that define a man \
who has inherited (or honed\
                   ) the suite of Dark \
Triad traits. He is closest \
to the manifestation of the ideal \
uncaring asshole.</p>\
<\
p>Reader Ripp writes:</\
p>\
<blockquote><p\
><em>“The Dark Triad \
are the component parts of the \
one overarching attitude that most defines \
and forges the successful womanizer: \
    overconfidence.”</em></p\
    >\
<p>Agreed\
,  academically. To qualify overconfidence\
:</p>\
<p>\
The art of exhibiting these qualities \
is commonly misrepresented by being a \
deliberate asshole; a ‘caring \
asshole’. Irrational overconfidence,  or \
‘cockyness’,  doesn’t \
hit the mark.</p>\
\
<p>Calculated arrogance,  \
effectively demonstrated pre-selection,  \
a refined non-reactive attitude \
to shit testing and a mysterious \
self-serving aloofness comprises the \
“attitude” described above.</\
p>\
<p>Uncalibrated \
“overconfidence” is try hard\
. Yielding true overconfidence at the \
correct moments hits the mark:</\
p>\
<p>“Listen\
. I don’t know \
you…and you need to \
understand. I’m one \
charming mother fucker.”</p></\
blockquote>\
<p>This \
reader has a point. If \
you have to shout your overconfidence \
from the rooftops,  you have \
shown the exact opposite: a \
lack of self-confidence.</\
p>\
<p>But \
most Dark Triad Dudes are <\
a href="https://heartiste\
.wordpress.com/2012\
/01/18/overconfidence\
-is-the-heart\
-of-game/" target\
="_blank"><em>irrationally\
</em> overconfident</a\
>,  if by irrational we mean \
that there is very little objective \
evidence that would buttress a case \
for their degree of self-\
regard. The reason they do \
well with women is because women \
don&#8217;t <\
em>subconsciously</em> \
care as much for objective measures \
verifying a man&#8217;\
s overconfidence as they care for \
the overconfident attitude itself. And\
,  remember,  when we&#\
8217;re talking about sparking \
vaginal tingles,  it&#8217\
;s a woman&#8217\
;s subconscious you want to \
massage,  not her conscious awareness\
. The subconscious is orders of \
magnitude more powerful than the conscious\
,  in which the latter pretty \
much acts as a highly advanced \
rationalization machine permitting expression of the \
desires of the subconscious.</p\
>\
<p>Again&#\
8230; it&#8217;\
s the <a href="\
https://heartiste.wordpress.\
com/2012/03/\
08/the-aloof-\
alpha-attitude-explained/" \
target="_blank">ALPHA ATTITUDE\
</a> chicks dig. \
You have the attitude,  and \
you can pretty much roll with \
any undersized or overstuffed portfolio of \
objective accomplishments. If you don\
&#8217;t have the \
attitude,  you will be dismayed \
to find that your <em\
>curriculum vitae</em> \
is not helping you get laid \
as much as the numbers you \
crunched told you it would help\
.</p>\
<p>\
Naturally,  it&#8217;\
s better to have both aligned \
&#8212; you&#8217\
;ll find it easier to \
maintain congruence if your objective status \
matches your signaling status &#8212\
; but if you had to \
choose one,  choose signaling status\
. It&#8217;s \
way simpler to achieve,  and \
more fun to apply!</p\
>\
<p>I&#\
8217;ll give you a \
quick glimpse at a minute in \
the life of a caring asshole\
,  so that you can better \
appreciate why he fails with women \
while his equal but different douchehead \
cousin cleans up with the ladies\
.</p>\
<p>\
Girl: &#8220;I \
don&#8217;t give \
my number to guys I just \
met.&#8221;</p>\
\
<p>Asshole who cares \
too much: &#8220;\
Well,  fuck you,  nobody \
asked for it.&#8221;</\
p>\
<p>Girl\
: &#8220;You just \
did.&#8221;</p>\
\
<p>Asshole who cares \
too much: &#8220;\
I was kidding. I would \
never go out with a bitch \
like you.&#8221;</p\
>\
<p>There&#\
8217;s no denying this \
guy is an asshole,  and \
there&#8217;s no \
denying he would be a miserable \
failure with women (although,  \
                    it has to be said\
                    ,  he&#8217;\
                    d still do better than \
                    the typical mincing betabot). \
So where did his assholery go \
wrong? For that,  we \
need to contrast him with his \
uncaring asshole bro.</p>\
\
<p>Girl: &#\
8220;I don&#8217\
;t give my number to \
guys I just met.&#8221\
;</p>\
<p>\
Asshole who cares thiiiiiiis much: \
    &#8220;My heart \
    will go on.&#8221\
    ;</p>\
<p\
>Girl: &#8220;Well,  you did seem like \
you wanted it.&#8221;</\
p>\
<p>Asshole \
who cares thiiiiiiis much: &#\
8220;That was before I \
got distracted by your sister.&#\
8221;</p>\
<p\
>In every technical aspect,  \
and according to every feminist by\
-law,  this guy would \
qualify as an asshole. And\
,  yet,  there&#8217\
;s just something about him\
&#8230;.</p>\
<\
p>wait&#8230; \
phew&#8230; I channeled \
some woman&#8217;s \
hamster there for a minute. \
Strange experience.</p>\
<\
p>The second guy knows \
about charm and delivery,  and \
executes with purpose. That purpose \
being,  to reflect,  &#\
8220;Goddamn,  I am \
a sexy beast. A stylish \
sniper of love. Excuse me \
whilst I make 1080p love to \
myself.&#8221;</p>\
\
<p>He is as \
far from your typical niceguy as \
he is from your hothead asshole \
above who calls women bitches at \
the drop of a hat. \
But an asshole he is,  \
and the right kind of asshole\
,  the kind that women,  \
the world over,  will always \
and forevermore fall head over haunches \
for despite their squid-inking \
claims to the contrary.</p >
'


gs12 = epub.EpubHtml(title='direct game essentials',
 file_name='direct_game_essentials.xhtml',
lang='en')
gs12.content='\
<h2>Direct Game Essentials</h2>\
<p>A reader wants\
to know if high octane direct\
game will get a guy laid\
consistently.</p>\
<blockquote\
><p>I stumbled <\
a href="http://www\
.pick-up-artist\
-forum.com/thinking\
-with-your-dick\
-vt126171.html" target\
="_blank">onto this post\
</a> during my normal\
stroll through the pick up artist\
forums.</p>\
<p\
>He claims to basically be\
completely direct with his game.\
I&#8217;ve never\
heard of people being THAT direct\
. Telling a girl she&#\
8217;s sexy like that\
,  seems a bit awkward and\
douchey.</p>\
<p\
>I&#8217;m\
mailing you because I&#8217\
;m curious what do you\
think? Could being so direct\
get great results?</p></\
blockquote>\
<p>I\
won&#8217;t get\
into a long-winded discussion\
of the eternal question of direct\
vs. indirect game here.\
I&#8217;ll save\
that for future posts. But\
I will tell you that there\
are a handful of prerequisites &#\
8212; essentials &#8212;\
that you should abide if you\
want to see any sort of\
repeatable success with direct game.</\
p>\
<p>1\
. Don&#8217;t\
be shitfaced.</p>\
<\
p>Yes,  the guy\
in the field report linked by\
the reader was intoxicated,  and\
he managed a groping make-\
out and a number close.\
But most men,  most of\
the time,  are going to\
get blown out if they approach\
chicks sloppy drunk while sputtering how\
&#8220;sexxxxxyyy&#8221\
; they are. It&#\
8217;s simply too easy\
for a girl to brush off\
a man&#8217;s\
direct come-on if he\
&#8217;s reeking of\
liquor and slurring his words.\
Exception: if she&#8217\
;s equally drunk. (\
    Not to say a little\
    liquid courage won&#8217\
    ;t help. Just\
    don&#8217;t\
    drink past the point of\
    self-awareness.)</p\
>\
<p>2.\
Don&#8217;t target\
the obnoxious attention whores.</p\
>\
<p>These kinds\
of girls are *expecting*\
direct solicitations,  just so they\
can relish the shoot down.\
Counterintuitively,  it&#8217;\
s often the more reserved,\
conservatively dressed girls who are showing\
a little more skin than they\
usually do who will crumble like\
feta cheese under the onslaught of\
a sexual direct approach. It\
is a myth that only skanks\
are DTF. Good girls will\
jump into the sack just as\
fast with the right guy spitting\
the right game.</p>\
\
<p>3. Look\
for signs of ovulation in your\
targets.</p>\
<p\
>You should pay more attention\
to body language than to what\
she&#8217;s saying\
. Ovulating girls are the ripest\
picks for one night stands,\
and you&#8217;ll\
notice by how flushed she is\
when talking to you,  how\
many times she crosses her legs\
or shifts her weight from one\
foot to the other,  and\
how often she licks her lips\
or tugs at her hair whether\
her egg has embarked on its\
journey. Science has shown that\
ovulating girls tend to show more\
cleavage and thigh,  so keep\
an eye out for miniskirts and\
low cut tops.</p>\
\
<p>4. Start\
direct,  then switch to indirect\
,  then back to direct.</\
p>\
<p>Read\
the linked field report. You\
&#8217;ll notice the\
guy opens with &#8220;\
You&#8217;re sexy\
as fuck&#8221; (\
which,  btw,  is NOT\
an invitation to fuck a la\
<a href="https://\
heartiste.wordpress.com/\
2009/06/19/\
i-tried-the-\
apocalypse-opener/" target="\
_blank">the apocalypse opener</\
a>),  then downshifts to nonsexual\
rapport and teases her about her\
dancing skill,  and then upshifts\
to a direct sexual solicitation when\
body contact between the two of\
them is at its maximum.\
This direct-indirect-direct\
system sustains the direct sexual approach\
by introducing the variables of male\
unpredictability and outcome independence,  two\
things which all girls love in\
men.</p>\
<p\
>5. It&#8217\
;s obvious,  but bears\
repeating: overconfidence is king in\
direct game.</p>\
<\
p>Any hint &#8212\
; I mean ANY CRUMB of\
a hint &#8212; that\
your sexually aggressive come-on\
is a farce,  or was\
pursued with less than full sincerity\
,  and she will blow you\
out. You have to be\
doubtless in your desirability,  fearless\
in your attack,  and dauntless\
in your commitment to victory.\
She smells the faintest whiff of\
self-doubt,  hesitancy or\
smarmy backpedaling,  and you will\
be pissily rejected.</p>\
\
<p>6. Avoid\
romantic flattery.</p>\
<\
p>&#8220;You&#\
8217;re sexy as fuck\
&#8221; sounds like a\
cocky compliment from a guy who\
just wants to jackhammer your pussy\
. &#8220;I have\
to say you&#8217;\
re really beautiful&#8221;\
sounds like a sycophantic plea from\
a beta who already dreams about\
long walks on the beach with\
you. Which guy do you\
think a girl is more likely\
to want to fuck one hour\
after meeting? You can pull\
off the latter with alpha body\
language,  but you&#8217\
;re better served maximizing congruency\
between what you say and how\
much command you say it with\
.</p>\
<p>\
7. Be prepared to lead\
,  every second.</p>\
\
<p>A guy who\
leads a girl everywhere and all\
the time prevents her from rethinking\
her desire to sleep with him\
. A body in motion tends\
to stay sexually available unless acted\
upon by a fat cockblock.\
Never ask. Tell her what\
you two are doing,  and\
don&#8217;t wait\
for a decision-making caucus\
to develop. Bar,  dance\
floor,  another bar,  another\
bar,  alleyway,  doorstep.\
No rest for the horny.</\
p>\
<p>8\
. Don&#8217;t\
<a href="https://\
heartiste.wordpress.com/\
2010/07/26/\
overgaming/" target="_blank">\
overgame</a>.</p>\
\
<p>Direct game pares\
down the seduction process to its\
bare bones. If you start\
flying off on tangents like &#\
8220;the cube&#8221\
; or storytelling,  the raw\
sexual energy of the direct pickup\
will dissipate. A girl relinquishing\
herself to a sexually aggressive man\
expects it to feel like a\
power has taken hold over her\
conscious faculties and she has no\
defense to his wiles. This\
is an accelerated zone of seduction\
where the normal rules get truncated\
.</p>\
<p>***</\
p>\
<p>The relevant question\
to everyone reading here is,\
of course: Will I have\
more success on a more consistent\
basis with direct game,  or\
with indirect game?</p>\
\
<p>Unfortunately,  I\
can&#8217;t answer\
this reasonable question with conviction one\
way or the other. My\
own personal style is indirect,\
though I have dabbled with direct\
game,  to mixed results.\
Most of the seduction community practices\
indirect game,  so if popularity\
is a measure of a game\
strategy&#8217;s effectiveness\
,  then you&#8217;\
d have to give the nod\
to indirect game. (Direct\
                   gamers would counter that indirect\
                   is popular with most men\
                   because it takes more balls\
                   to pull off direct game\
                   . They have a point\
                   .)</p>\
<p\
>There are other variables that\
need addressing before we can settle\
this matter one way or the\
other.</p>\
<p\
>&#8211; Are very good\
-looking or muscular men better\
off running direct or indirect game\
? The answer to this is\
not obvious.</p>\
<\
p>&#8211; What about\
significantly older men or uglier men\
or shorter men? Indirect game\
may limit the number of blowouts\
experienced by these men. Conversely\
,  direct game may offer them\
a channel in which to rapidly\
demonstrate their overconfidence,  thus bypassing\
the reflexive blowout. Again,\
the answer is not obvious.</\
p>\
<p>&#8211\
; Are there contexts in which\
direct and indirect game have inherent\
advantages? My experience is that\
girls respond better to indirect during\
the day and direct at night\
in clubs,  but I don\
&#8217;t have a\
wealth of direct day game data\
to test this hypothesis.</p\
>\
<p>&#8211;\
Do some kinds of girls respond\
better to direct? Indirect?\
Unsurprisingly,  a man I once\
knew who specializes in cougars (\
    it&#8217;s\
    not a difficult specialization)\
says that older women melt for\
his direct game. Ovulating coke\
whores with <a href="\
https://heartiste.wordpress.\
com/2011/11/\
30/does-game-\
work-less-well-\
on-masculine-women/"\
target="_blank">low digit\
ratios</a> probably swoon\
for direct game,  as well\
.</p>\
<p>\
Finally,  this dichotomy of direct\
versus indirect may have outlived its\
usefulness. Thinking on my pickups\
,  it occurs to me that\
many of them were mash-\
ups of direct and indirect game\
. I use the best of\
both. Then there&#8217\
;s the definitional issue:\
    direct game comes in many\
    forms. &#8220;\
    You&#8217;re\
    sexy as fuck&#8221\
    ; is certainly direct,\
    but it&#8217;\
    s not an invitation to\
    fuck. There&#8217\
    ;s plausible deniability of\
    intention in that exclamation.\
    &#8220;I want\
    to take you home and\
    fuck you&#8221;&#\
    8230; now,  that\
    &#8217;s a\
    direct come-on which\
    leaves no room for hamster\
    -fueling misinterpretation.</p>\
<p>And this gets to the heart\
of the direct-indirect debate\
: namely,  INTENTION. Direct\
game is the art of communicating\
your intention to fuck,  sooner\
and stronger rather than later and\
weaker. Indirect game is the\
art of transparently concealing your intention\
to fuck in a cloak of\
plausible,  yet tissue-thin\
,  deniability. Either way,\
with direct or indirect,  a\
girl whose social IQ is above\
room temperature and below genius-\
level autism is going to know\
you are talking to her because\
you eventually want to ravage her\
naked body. Your job,\
should you choose to accept it\
,  is to determine who among\
the pretty constellation of hot babes wants their\
seduction straight up smashmouth\
style,  and who among them\
wants to experience the sublime thrill\
of fraught flirtation.</p>
'


gs13 = epub.EpubHtml(title='generalizing your way into her panties',
 file_name='generalizing_your_way_into_her_panties.xhtml',
lang='en')
gs13.content='\
<h2>Generalizing Your Way Into Her Panties</h2>\
<p>Reader JB emailed \
me with a valuable observation about \
the effectiveness of using generalizations as \
a game tactic. He read \
my post <a href="\
https://heartiste.wordpress.\
com/2008/03/\
27/dread/" target="\
_blank">&#8220;Dread&#\
8221;</a> where I \
explain the best ways to train \
your girlfriend so that you maximize \
love output and minimize shit test \
incitement:</p>\
<blockquote\
><p>Ignore her calls \
for a week. When you \
eventually answer and she reads you \
the riot act,  act as \
if nothing was wrong and accuse \
her of sabotaging a perfectly good \
relationship,  <em>&#8220\
;just like all the other \
women in this stupid city. \
I thought you were different&#\
8221;.</em> Hang up \
on her angrily.</p></\
blockquote>\
<p>JB \
wrote:</p>\
<blockquote\
><p>When I read \
this I fucking almost spit up \
my mouthful of coffee. Funny \
because it&#8217;s \
true. Have you written anything \
about the powerful effect generalization has \
on the female psyche? I \
have used the &#8216;\
you&#8217;re just \
like every other girl in this \
city&#8217; one and \
BANG!<br />\
No matter \
who the girl,  no matter \
the age&#8230;she \
stops cold and finds herself waiting \
for what I&#8217;\
m going to say next.</\
p>\
<p>Good \
stuff,  keep it up.</\
p></blockquote>\
<p\
>Yes,  it&#8217\
;s true. Throwing a \
generalization in the face of a \
girl you are gaming by accusing \
her of being &#8220;\
just like all the rest&#\
8221; is a powerful qualification \
tactic. It will send her \
into paroxysms of indignation and self\
-doubt as she works hard \
to regain your approval.</p\
>\
<p><strong>\
Maxim #33: NO girl \
wants to be thought she isn\
&#8217;t a special \
little snowflake.</strong></p\
>\
<p>Use this \
thermal exhaust port of female psychology \
to your advantage. But be \
careful how you deploy the generalization \
bomb &#8212; its mindfuck \
megatonnage can blow up chicks&#\
8217; heads like scanners. \
There are two ways to laser\
-guide a generalization straight into \
the beaver bunker.</p>\
\
<ol>\
<li><\
strong>Exasperation.</strong> \
See the example above. Can \
be useful in pickup as well \
as relationship management &#8212; \
for instance,  after she&#\
8217;s started acting up \
and attempted to find your soft \
underbelly. In pickup parlance,  \
this would be during the M2F \
attraction phase. Watch as she \
spins her wheels trying to prove \
her uniqueness.</li>\
<\
li><strong>Reverse psychology\
.</strong> Right before you \
run a routine with her,  \
like palm reading or astrological compatibility\
,  tell her she&#8217\
;s probably like all the \
other girls in [insert city\
                ] and wouldn&#8217\
;t appreciate the deep and \
profound knowledge you are about to \
drop on her. If she \
says &#8220;What do \
you mean I&#8217;\
m like all the rest?!&#\
8221;,  you reply &#8220\
;Tell me I&#8217\
;m wrong.&#8221;</\
li>\
</ol>\
<\
p>I don&#8217\
;t just dispense advice,  \
I explain *why* the \
advice works,  stripping away the \
mystery and spirituality squid ink with \
the sandblaster of biomechanics,  so \
you can see for yourself the \
predictability of the human attraction algorithm\
.</p>\
<p>\
As I wrote in response to \
Clio in the comments section of \
<a href="https://\
heartiste.wordpress.com/\
2008/09/29/\
supermodels-are-not-\
hot/" target="_blank">\
this post</a>:</p\
>\
<blockquote><p>\
here is what i think motivates \
the female will to believe that \
makeup is effective at hiding flaws \
from the precision guided instrument of \
men’s visual intake port\
:</p>\
<p>\
the fear of the immutable.</\
p>\
<p>if \
you’ll notice,  women \
are the most outraged by the \
idea of evolutionary psychology and unchangeable \
genetic fate. that physical beauty \
should be so unalterable and at \
the same time so critical to \
a woman’s prospects for \
snagging an alpha male of her \
own sends shivers down her spine\
. if true,  it means \
they cannot do much to improve \
their value on the open market\
. no educational attainment,  no \
carreer success,  no makeup,  \
no exercise [to a point\
            ],  no hob nobbing with \
the right people — nothing much \
matters but for the face they \
were given when mommy’s \
egg was fertilized by daddy’\
s swimmers.</p>\
<\
p>yet,  this is \
precisely how the sexual market works\
. and so,  as the \
gears of the pretty lie machine \
clank and sputter to dispense more \
of its life-affirming self\
-delusions,  the “social \
conditioning” brigade strikes out at \
the descending shroud of hopeless darkness\
.</p></blockquote>\
<\
p>Generalizations offend women in \
a way they do not offend \
men because they breach the perimeter \
ego defense and strike right at \
a woman&#8217;s \
core self-conception &#8212\
; her belief in herself as \
Princess On A Cloud Carried Aloft \
By Admiring Suitors. If it\
&#8217;s true that \
her genes account for nearly all \
her success or failure with the \
men she wants,  then there \
isn&#8217;t much \
she can do to improve her \
chances to fulfill her deepest desires\
. If it&#8217;\
s true (and it is\
    ) that men value beauty \
above all else,  then it \
is logically inescapable that she is\
,  to an unsettling degree,  \
interchangeable with any women who are \
at or above her level of \
physical attractiveness.</p>\
<\
p>Women do not want \
to confront the unpleasant reality of \
upwardly immutable female sexual market value\
. (They can certainly go \
down in market value by \
bloating up or suffering a \
facial disfigurement.) Similarly,  \
they do not want to admit \
they aren&#8217;t \
special. So they fight against \
it. They hide behind pretty \
little platitudes and try to correct \
your misperceptions to the contrary. \
Deep in the primitive ancestral part of her reptilian brain she fears\
,  justifiably,  that if she \
isn&#8217;t a \
unique creature in your eyes,  \
you may be likely to leave \
her if a hotter woman blips \
your radar. FOR INNATE EVOLUTIONARILY \
MODULATED REASONS,  SHE WANTS TO \
KNOW YOU SEE MORE IN HER \
THAN HER BEAUTY. You should \
leverage this female instinct to your \
benefit.</p>\
<p\
>&#8220;So what else \
do you have going for you \
besides your beauty?&#8221;</\
p>\
<p>If \
you are the one special suitor \
who wrings her princess cloud dry \
and sends her plummeting to earth \
with a well-timed generalization \
that belies her uniqueness,  she \
will suddenly find,  in violation \
of the courtship script she was \
so used to following,  an \
inexplicable urge to seek *your\
* approval,  and demonstrate for \
*you* how different she \
is from other women and how \
you just *have to* \
see that.</p>\
<\
p>Then,  my friend,  you will be in the driver&#8217;s seat. Zoom zoom.</p>
'


gs14 = epub.EpubHtml(title='are you seeing anyone',
file_name='are_you_seeing_anyone.xhtml',
lang='en')
gs14.content='
<h2>Are You Seeing Anyone</h2>
<p>A reader emails:</p>
<blockquote><p>Really loved the &#8220;<a href="https://heartiste.wordpress.com/2010/05/26/two-words-women-love-to-hear/" target="_blank">it&#8217;s complicated</a>&#8221; post,  and have found lots of versatile use for it in my life. Thinking about it though,  I think it&#8217;s most effective with women new to you as opposed to women you have history with. I also don&#8217;t think it should be used as a text response. Some of my ex&#8217;s will hit me up out of the blue via text,  usually playful messages,  but sometimes with the direct inquiry &#8220;are you seeing anyone?&#8221; that only a woman (or clueless beta orbiter) would ask. While &#8220;it&#8217;s complicated&#8221; would now be my default response to a new girl at a bar if she asked the same,  I think it sounds too defensive and pandering to an ex,  as though you&#8217;re trying to hide something from someone who already knows you very well. <strong>[Ed: Agreed.] </strong>I also think it doesn&#8217;t have the same effectiveness if used as a text reply to anyone.</p>
<p>I went with this exchange recently:</p>
<p>aspirational ex-girlfriend: Are you seeing anyone?<br />
(next morning) me: you workin for tmz now?</p></blockquote>
<p>Good answer. Cocky and funny,  jes like da ladeez like it. She also appreciates the haphazard attention to punctuation.</p>
<p>&#8220;Are you seeing anyone?&#8221; is a common enough question from interested women that the proper handling of it deserves its own post. (Rumor has it there are a lot of sniveling gameless betas who ask women this question when they first meet them. Pitiable creatures.)</p>
<p>If an ex-girlfriend,  former fuckbuddy or platonic female friend who you think wants to revisit the good times with you,  (or who simply wants to segue from friendship to sex),  asks if you are seeing anyone,  and you have decided that &#8220;it&#8217;s complicated&#8221; is not the best response,  there are alternatives at your disposal.</p>
<p>1. Sincerity</p>
<p>&#8220;I&#8217;ve been dating someone for a bit,  but I can&#8217;t say for sure she is the one.&#8221;</p>
<p>2. Lying</p>
<p>&#8220;No.&#8221;*</p>
<p>3. Evasion/Reframing</p>
<p>See: the reader&#8217;s reply above. Few women will follow-up an expertly delivered evasion with cunty lawyerly argumentation. This is because women who ask such questions don&#8217;t really want to know the unvarnished answer. The question is asked only to give them plausible deniability should they find themselves bedding a taken man.</p>
<p>4. Circumspection</p>
<p>&#8220;I&#8217;m dating around.&#8221;</p>
<p>This is my favorite answer,  regardless of its accuracy. First,  it shuts down further inquiry. Second,  it leaves things open to interpretation.</p>
<p>5. Challenge</p>
<p>&#8220;I&#8217;m not tied down yet.&#8221;</p>
<p>6. Agree &amp; Amplify</p>
<p>&#8220;One?&#8221;</p>
<p>7. Aloofness</p>
<p>&#8220;Nothing serious.&#8221;</p>
<p>Also a personal favorite. Girls like to think the guys they desire have no worries about meeting and banging women,  or about settling down.</p>
<p>*&#8221;No&#8221; is not the ideal reply. Because of the power of preselection,  you run a better chance of losing her interest if she thinks you are completely single than you do if she thinks you are getting pussy regularly. So even if you aren&#8217;t seeing anyone,  you should massage your answer so that ambiguity is introduced to the dialectic. Women aren&#8217;t put off a man&#8217;s scent if he is seeing someone; if anything,  they become more like a bloodhound on his trail. The only exception is when the man sings odes of love and devotion to his woman. Competitor women will generally** back off if they see that the man they want is truly,  deeply in love with someone else.</p>
<p>**Before the fairy dust,  pie in the sky,  swoon brigade gets all gushy at this optimistic outlook on the female gender,  let me remind the studio audience that I have observed,  and experienced,  plenty of exceptions to this rule.</p>
<p><span style="text-decoration:underline;">Replies that you should avoid:</span></p>
<p>&#8220;Define &#8216;seeing&#8217;.&#8221;</p>
<p>Too goofy. Chicks don&#8217;t dig the goof.</p>
<p>&#8220;Not sure.&#8221;</p>
<p>Too indecisive. Chicks don&#8217;t dig vacillators.</p>
<p>&#8220;Well,  I&#8217;m fucking someone,  if that&#8217;s what you mean.&#8221;</p>
<p>Too visual and sexual. Chicks don&#8217;t dig braggarts.</p>
<p>&#8220;I&#8217;m married.&#8221;</p>
<p>Too final. Chicks need a window of opportunity.</p>
<p>&#8220;Aren&#8217;t you the nosy one?&#8221;</p>
<p>Too slippery and awkward. What are you hiding?</p>
<p>&#8220;Wouldn&#8217;t you like to know.&#8221;</p>
<p>Too abrasive. If she&#8217;s an ex who knows you well,  this albeit funny line will close off further exploration.</p>
<p>&#8220;Why do you ask?&#8221;</p>
<p>Too defensive. Also,  why would you step on her hamster right as its revving up for a glorious rationalization to sleep with you?</p>
<p>Commenters are available during business hours to help you with further suggestions.</p>
'


gs15 = epub.EpubHtml(title='fine art of teasing',
file_name='fine_art_of_teasing.xhtml',
lang='en')
gs15.content='
<h2>Fine Art Of Teasing</h2>
<p>An important facet of game &#8212; whether for relationships,  flings or pickups &#8212; is fluency with the art of teasing. Teasing is such a turn-on for women it&#8217;s a wonder it isn&#8217;t taught by marriage counselors. (Actually,  it&#8217;s not a wonder. As the divorce statistics show us,  marriage counselors have no fucking clue what works.)</p>
<p>Here&#8217;s an example of what I mean by teasing:</p>
<p>ME: Don&#8217;t worry. If I got famous I wouldn&#8217;t drop you like a hot potato.</p>
<p>HER: Gee,  thanks. That&#8217;s so sweet.</p>
<p>ME: I&#8217;d wait a couple months.</p>
<p>HER: Jerk! *playful punch*</p>
<p>You should be teasing your girlfriend or wife like this nearly every day of her life. Women LOVE LOVE LOVE men who don&#8217;t take them seriously. And what better way to convey an aloof disregard for her pride than through teasing?</p>
<p>I&#8217;d like to examine the phenomenon of teasing a little more closely. Why,  exactly,  does it so effectively light up a woman&#8217;s arousal bean? After all,  teasing is not flattery or compliments. It&#8217;s nearer the opposite: teasing is a form of put-down. Compare and contrast the below with the teasing example above:</p>
<p>ME: If I got famous I&#8217;d trade up from you to a hotter babe in about two month&#8217;s time.</p>
<p>HER: Whaaat?! [angry,  hurt]</p>
<p>This example is no different in substance than the teasing example above,  yet the latter provokes anger and withdrawal while the former provokes tingles. The key difference between the two interactions lies in the concept of <strong>butthurtness</strong>.</p>
<p><strong>butthurtness</strong>; <em>noun</em><br />
an emotional state of being characterized by spite,  bitterness and/or insecurity; highly toxic to female attraction.</p>
<p>Teasing is the art of delivering ugly truths in a charismatic style that inoculates the teaser against an accusation or perception of butthurtness.</p>
<p>The truth value of whatever you are teasing a girl about is immaterial; it&#8217;s *how* you say it that matters. It may very well be true that should you become famous you would dump your girlfriend for a hotter girl,  or that her sense of humor sucks,  but that&#8217;s irrelevant to the way in which such information is conveyed to her. If you can say it with a smirk,  and couch your jerkish thoughts in the veneer of playful fun,  she will register your demeanor as being one that an alpha male possesses. And this daily revelation will engorge her labia.</p>
<p>If you don&#8217;t know how to tease,  then your jerkish blurts will be perceived by her as those held by a nasty beta secretly afraid she might leave him.</p>
<p>Teasing is a vital game tactic that serves the dual functions of 1) making relationships and dates less boring,  and 2) subtly reminding the girl that you have options and aren&#8217;t afraid to risk her disapproval,  which is the hallmark of the desirable alpha male swimming in a sea of snatch.</p>
<p>All of this &#8212; women&#8217;s love for jerks who know how to tease &#8212; ultimately reduces to the sexy son hypothesis,  which has been explained in <a href="https://heartiste.wordpress.com/2009/01/12/a-hole-game-day-1/" target="_blank">previous posts</a>.</p>
'


gs16 = epub.EpubHtml(title='the clas clown puts her in the mood',
file_name='the_class_clown_puts_her_in_the_mood.xhtml',
lang='en')
gs16.content='
<h2>The Class Clown Puts Her In The Mood</h2>
<p>&#8230;for laughing. </p>
<p>I&#8217;m not a fan of goofball humor to attract girls.   She&#8217;ll laugh her way straight into a platonic friendship with you.  This is especially true during the critical first few minutes of meeting her when you are trying to get her to ponder the possibility of sleeping with you.  Droll,  clever humor,  dispensed sparingly,  is more effective.  Playful humor,  or teasing,  turns girls on as well.  Acting like a clown and constantly joking sends a subliminal message to the sex centers of her brain &#8212; <strong><em>He&#8217;s trying too hard.  He must be desperate for female attention.</em></strong></p>
<p>Self-deprecating humor is the worst kind.  Only men possessing the traits that women love can afford to knock themselves down in a humorous fashion.  It&#8217;s similar to the way wealthy men make sure their philanthropy is reported in the press; it&#8217;s a status display that is very attractive to women because it shows he is financially secure enough to absorb a hit to his resources.  For most men,  though,  self-deprecation is beta.</p>
<p>Cheesy humor has its place.  It can often work quite well as an opener under the right circumstances.  It won&#8217;t work in clubs,  where loud music and physical jostling compete for a girl&#8217;s attention,  and where she is already smiling and expecting to be hit on.  There,  your humor will strike her as a lame come-on.  But out on the street,  or in a store,  during the daytime,  weird humor can win you an audition with her.  She&#8217;s not expecting to be approached,  she&#8217;s probably in a hurry somewhere,  so an offbeat line will put a smile on her face.  Distracting a girl from her orderly existence is the first step to fornication.  Some lines I have used:</p>
<blockquote><p><em>I *love* the way you pour ice cubes into a glass.  </em>[spoken to a female bartender]</p>
<p><em>You jaywalk with a certain grace.  </em>[girl had crossed intersection and was standing next to me]</p>
<p><em>Is there a groom magazine?  I can&#8217;t get enough of weddings!</em>  [to girl reading Bridal Magazine in bookstore.  she was single]</p>
<p><em>Did you just undress me with your eyes?  I feel violated.</em>  [to seamstress measuring a suit for me]</p>
<p><em>My puppy ran away with the poolboy.  Will you give me a new one?  You don&#8217;t want to see me cry.</em>  [to Adopt-A-Pet girl showing shelter animals on sidewalk]</p>
<p><em>Rearrange these five straws into something round. </em> [straws are lined up side by side]  <em>But you can only move two of them.</em>  [waitress makes attempt and fails]  <em>Here,  let me show you.</em>  [I move two straws and make the word TIT]</p>
<p><em>Slow down!  You deserve a chance to check me out.</em>  [to girl walking quickly towards me]</p></blockquote>
<p>I know the girls reading this right now are thinking &#8220;if a guy said that to me,  I would laugh at him,  not with him&#8221; but reading about pick up lines on a blog is not the same as hearing it in real time when it&#8217;s totally unexpected.  Nevertheless,  you don&#8217;t want to be a stand-up comedian.  Those guys are entertainers,  not seducers.  I wouldn&#8217;t use dorky humor as a general purpose opener.  It has limited application.  The classic openers &#8212; asking for her opinion on female-friendly topics,  situational observations,  flirty cockiness &#8212; are staples.  They&#8217;ll work in almost any scenario.</p>
<p>If you are a woman with a great sense of humor (you do exist,  somewhere) I suggest you hide it during the first few dates with a guy.  Most men are intimidated by women they&#8217;re dating who are funnier than them.  And intimidated guys don&#8217;t satisfy sexually.</p>
'

gs17 = epub.EpubHtml(title='the devious takeaway',
file_name='the_devious_takeaway.xhtml',
lang='en')
gs17.content='
<h2>The Devious Takeaway</h2>
<p>Note: what I&#8217;m about to write here is not meant for game newbies. Utilize at your own risk.</p>
<p>Takeaways are a very valuable psychological ploy contributing to a player&#8217;s seduction prowess. You can read a <a href="http://www.fastseduction.com/cgi-bin/fswiki.cgi?Takeaway" target="_blank">definition of takeaways here</a>. In short,  a takeaway is the act of feigning disinterest in a woman for the purpose of increasing her attraction for you,  and thus your likelihood of bedding her. This fake disinterest can be as simple as a backturn,  or an unannounced abrupt exit from a conversation. Takeaways are the Swiss Army knives of seduction,  as they can be used at almost any point during the pickup,  with equal effectiveness. For instance,  a takeaway can set the right tempo early on by making a girl chase you for conversation instead of the other way around,  or a takeaway can be employed during foreplay to get a girl to drop her last minute resistance to sex.</p>
<p>Takeaways are a very powerful game tactic,  for the reason that they are a high risk gamble. (Generally,  and as with most things in life,  the riskier the game tactic,  the higher the reward.) The risk comes in the fact that a girl may very well call your takeaway bluff.</p>
<p>PLAYER: You&#8217;re really cool and all. Maybe we should just be friends.</p>
<p>GIRL: Ok.</p>
<p>But when a takeaway works,  and the girl bites,  you will be amazed at how quickly the status dynamics of the courtship will change. Flipping the script,  properly executed,  can make gaming a girl seem like outrunning a morbidly obese American woman. You can practically walk to the finish line.</p>
<p>Here&#8217;s an especially devious takeaway that I&#8217;ve used many times to great effect. Use this on later dates just before the momentum is carrying you both to sexual closure,  and only use on girls who are engaging in stalling tactics. In other words,  use on &#8220;good girls&#8221;. (There is a minor subclass of bad girls who will also respond well to this takeaway,  which I will explain below.) Basically,  what you will be doing is stealing the woman&#8217;s prerogative to delay coital finality in the interest of &#8220;wanting everything to feel right&#8221;.</p>
<p>UNWITTING GIRL: I&#8217;m having a really good time.</p>
<p>DEVIOUS YOU: Me too. I&#8217;d like to have a drink with you back at my place,  but&#8230;</p>
<p>UNWITTING GIRL: What?</p>
<p>DEVIOUS YOU: I dunno. I&#8217;m trying to turn over a new leaf. I think it means a lot more when things aren&#8217;t rushed. Maybe wait a little. You&#8217;re the kind of girl I want to take it slow with. Call me crazy,  but that&#8217;s how I see it now.</p>
<p>Now after this,  most likely she will say &#8220;Aw that&#8217;s so nice&#8221; and agree with you. Then you will be left asking yourself,  &#8220;Hey,  I thought this was supposed to work as advertised? She just called my bluff!&#8221; Settle down,  Anakin. This takeaway works it&#8217;s magic on a delayed cycle. Continue the date as usual,  and invite her over to your place anyhow. You won&#8217;t need an excuse because you&#8217;ve already told her nothing will happen. What you&#8217;ll notice instead is an increase in her compliance that you would not normally have gotten. Though you &#8220;confessed&#8221; only hours earlier,  in so many words,  that you wanted to wait for sex,  she will find herself inexplicably moving things faster in the direction of your hidden agenda. The phony virtue takeaway has preemptively disarmed her anti-slut defense. She will rationalize that you are not forcing her to do anything because you&#8217;re &#8220;not that kind of guy&#8221;,  and your road to sex will suffer fewer impediments.</p>
<p>Why did I write above that this takeaway is not meant for newbs? Because you need to be banging other girls before attempting such a high risk maneuver. If you are hard-up,  your mind,  body,  and emotions will be incongruent with your spoken words. She will sense something is off about your claimed phony virtue,  and she will not only call your bluff,  but also lose respect for your now-waning masculinity for trying an end-run around her sexual reticence *and* your own sexual desire.</p>
<p>In addition,  some newbs may mistakenly use this takeaway on girls who are already good to go. That&#8217;s called overkill. If she genuinely wants it,  you won&#8217;t need any more mental games. All you&#8217;ll need at that point is the balls to lead her where she wants to be.</p>
<p>As I mentioned above,  the subclass of girls this takeaway would work on are the badgirl sluts who are practically dragging you to the bedroom. Be careful of the overtly sexual girls; oftentimes their lewdness and blunt physical sexuality are a ruse designed to entrap less alpha men who lack control over their horniness. If you bite too soon or too eagerly,  she may lose her desire. If you do manage to bed a badgirl slut on the first date,  she is more likely than the typical girl &#8212; thanks to the male-like contours of her brain &#8212; to lose interest the next morning. For these girls,  the phony virtue takeaway is perfect for (re)establishing that she is the one chasing you,  and not the other way around. Plus,  by stroking her egotistic need to not be noticed for her sluttiness,  it will make her feel more special than she really is. Phony virtue game,  delivered as sincerely as your acting skills can summon,  can turn a one night stand with a slut into a three month fling.</p>
'

gs18 = epub.EpubHtml(title='storytelling',
file_name='storytelling.xhtml',
lang='en')
gs18.content='
<h2>Storytelling AKA Fibbing</h2>
<p>In the course of your conversation with a woman you want to tell a story about yourself that flips those female attraction switches which Mystery so incisively described as &#8220;pre-selection by women,  leader of men,  and protector of loved ones&#8221;. But,  honestly,  how many men have those kinds of rip roaring yarns to tell which powerfully hit all those girl buttons? If you&#8217;re like most men,  you likely have not led the life of an international man of mystery.</p>
<p>And of those men who *do* have stories like that to tell,  how many of them are able to relay their stories for maximum impact? I&#8217;ve known quite a few Marines who spent time overseas in the middle of some crazy shit inexplicably tell their tales in such a way as to render them boring and ineffectual. You have to learn to sell yourself. Sometimes even top notch goods sit moldy on the shelves for lack of marketing and salesmanship.</p>
<p>This is where having a story (or a routine,  in old school parlance) memorized and ready for deployment is critical to a man&#8217;s success bedding women. There is nothing inherently beta or creepy about memorizing stories from your life to use over and over with different women. Alpha males,  indeed,  are the biggest violators of the supposed sanctity of extemporaneous jiving. If you&#8217;ve ever hung out at upper class parties and the like you&#8217;ll notice the top dogs returning to the same well again and again,  telling their stories in exquisite detail and precise manner,  using almost the same words and cadence each time,  because they have learned how to tell their best stories to ensure smiles and squeals of delight from their rapt audience. So go ahead and commit to memory one or two great stories that feature you in a starring role. Like a good Boy Scout,  you should always be prepared.</p>
<p>So what does the man without a great story do? Well,  my friend,  this is where knowledge of the fine art of fibbing will take you far. I&#8217;ll illustrate with an example from my own life. Let&#8217;s say you have just asked a girl a beaver baiting question like &#8220;If you could wake up tomorrow and be anywhere in the world,  where would it be?&#8221; She gets excited by this question and answers. This allows you to segue into a DHV story like the one from my life below.</p>
<p><span style="text-decoration:underline;">THE TRUE STORY</span></p>
<p>One of my vacations was at a tropical paradise. Sun,  sand,  waves,  fruity cocktails. After an uneventful plane ride,  I rented a scooter and rode to the villa I was staying at. I paid a taxi to take my luggage to the same spot. Upon settling in and admiring the ocean view for fifteen minutes,  I slathered on suntan lotion and trundled to a small beach alcove known for its nude sunbathers,  hoping to peep at boobies and snatch. Once there,  a couple of fat Europeans obstructed my view with their bloated nakedness. It turned me off. I moved down the beach away from them and read &#8220;A Portrait of the Artist as a Young Man&#8221;. Not the whole book,  just the first few pages. I&#8217;m a <span style="text-decoration:line-through;">slow</span> absorbent reader. Then I went in the water and bobbed like a buoy. At 4pm,  I walked to the tiki stand and bought a sandwich. On the walk back to the villa,  I took a photo of three locals unloading crates from a red and yellow dingy docked at a tiny,  empty beach. I watched them for a bit,  when one of the gentlemen bounded up the craggy hillside and stopped directly in front of me. He barked at me to &#8220;stop taking snaps of my boat,  mon.&#8221; Momentarily stunned,  I looked at him like he was an alien. Finally,  I said &#8220;Why? It&#8217;s legal.&#8221; He repeated himself,  and threatened to steal my camera. I said &#8220;Yeah,  sure,  whatever&#8221; and walked off. Back at the villa,  the concierge told me there was a drug running problem in these parts of the island,  and that I was lucky not to get knifed. Relieved by my good fortune,  I lounged at the pool until I fell asleep.</p>
<p>The next day,  I went scuba diving. I was part of an instructional group,  since I never scuba dived before. When I first plunged in the water I freaked out for a few seconds before gaining my composure and relaxing enough to breathe properly through the mouthpiece. A barracuda swam by me. It wasn&#8217;t very big or threatening. I could have petted it. Later in the afternoon I lounged at the beach again and ate another sandwich. The sandwich was delicious.</p>
<p>Day three. I decided snorkeling was more fun than scuba diving,  so I rented some snorkeling gear and floated on top of the azure waters for a few hours watching small iridescent fish swim around. I got a sunburn on my back. I went to a club that night and hit on two French girls. One was interested,  but she had a kid and an expensive coke habit.</p>
<p>Day four. More sunbathing. Oh yeah,  and I went into town to browse the electronics shops and the ridiculously overpriced French fashion boutiques. I bought some liquor. Back at the villa I made a plate of brie cheese,  baguettes,  and red wine. The cheese made me gassy.</p>
<p>Day five. I went on a deep sea fishing boat to see how it was done. The waves were huge. I got seasick. My face turned green and I chucked over the side of the boat. The tall skinny black man operating the boat laughed at me. So did the little kid sitting next to me.</p>
<p>Day six. Having had my fill of sunbathing,  I caught a ferry to a nearby island known for its excellent and invigorating hiking. The island was a dormant volcano that shot straight up out of the ocean. The hike was exhausting. 3, 000 feet up took me all day. I saw a lot of green tropical plants along the way,  and a couple of small lizards. I asked someone if the lizards were biters. They weren&#8217;t. I was disappointed. On the way down,  I stopped at a small store and bought a trinket made of amber from an old,  fat black woman.</p>
<p>Day seven. I went back to the same tiki stand,  because why mess with success? They had tasty sandwiches. On the plane ride home,  I jammed in earphones and listened to music.</p>
<p>***</p>
<p>Now this isn&#8217;t a horrible story,  but it&#8217;s not exactly a panty-dropper,  is it?</p>
<p><span style="text-decoration:underline;">THE FUDGED STORY INTENDED TO INCITE MAXIMUM GINA TINGLE</span></p>
<p>[Addressing girl]: Your ideal vacation spot reminds me of the time I went to [tropical island] and wound up with an adventure I hadn&#8217;t bargained for. I was chatting with some French girls at this supposedly exclusive nude beach &#8212; and by the way,  conversations take on a whole new feel when everyone is naked &#8212; when a big fat German dude plopped down right next to us. He was blocking out our sun like an eclipse,  so we decided to leave. Since they were staying at the same villa I was at,  I escorted them home. On the way,  I stopped to take a pic of this interesting boat docked at a quiet beach alcove. Suddenly,  one of the dudes unloading boxes from the boat bounded up the hillside and yelled at me to &#8220;stop taking snaps of my boat,  mon!&#8221; I said,  &#8220;What&#8217;s it to you&#8221; and he lunged at me and pushed a knife to my throat. The two French girls gasped. This was pretty scary. Thinking quickly,  I told him that wasn&#8217;t a good idea because a bunch of people were walking towards us right at that moment. When he turned around to look,  I grabbed one of the girl&#8217;s hands and dashed around him to safety just a few hundred yards away. He didn&#8217;t chase us. I told the cops about the incident,  but as far as I know nothing was done. There&#8217;s a drug running problem at that island,  and I got caught in the middle of it.</p>
<p>The unexpected adventure didn&#8217;t end there. I went scuba diving the next day and a shark that had to be ten feet long swam by me like a torpedo. The locals told me the sharks in those waters are harmless and won&#8217;t bother humans,  but when you&#8217;ve seen them up close like that you don&#8217;t really believe all that bullshit. It was thrilling,  sure,  but I think I prefer watching sharks on TV.</p>
<p>I needed a break from all this unwanted excitement,  so after an evening of red wine and French cheese while relaxing in the hot tub,  I planned a hiking trip to a remote volcanic island that could be reached by ferry. On the hike up the mountain through thick rainforest and heavy fog,  I stumbled across an old rickety shack with a sign outside that offered psychic services. Curious,  I stepped inside and was greeted by an old black woman with an incredible accent. I don&#8217;t believe in psychic stuff,  but I decided to let her read my fortune. Whatever it was,  it wasn&#8217;t good. She stood up and said the session was over. Then she handed me an amber medallion and said it was a soulstone,  which I should only give to a woman I will be with for the remainder of my life,  because the woman who receives it will then have a piece of my soul. I still have the stone.</p>
<p>Have you ever gone deep sea fishing? If you do,  take anti-seasickness pills. The waves were rocking the boat to the left and right. This boy sitting next to me was leaning over the railing trying to touch the flying fish when he got sick and started to slip over the side. I grabbed the kid before he fell into the ocean and told him to be careful. You&#8217;ve gotta wonder where this kid&#8217;s parents were just letting him take a deep sea fishing excursion by himself.</p>
<p>After all that,  I think I would have been better off just hanging out at Ocean City. But it wasn&#8217;t all bad. I picked up some French while I was down there.</p>
<p>***</p>
<p>Pre-selected by women? Nude French girls. Check.<br />
Protector of loved ones? Helped French girls escape drug lord. Check.<br />
Leader of men? Rescued boy from drowning. Check.</p>
<p>Much improved.</p>
<p>Don&#8217;t feel bad about fibbing. You are doing the exact same thing a woman does when she attempts to present her mating market value in the best possible light through the use of makeup and coy mannerisms. Seduction is an intricate weave of truth and fiction,  and women would have it no other way.</p>
'


gs19 = epub.EpubHtml(title='contrast is king',
file_name='contrast_is_king.xhtml',
lang='en')
gs19.content='
<h2>Contrast Is King</h2>
<p>Was sent this photo,  with the following message:</p>
<p>&#8220;First I saw the two barking rats,  then I saw the guy walking them. Talk about an odd pairing! The dude had tattoos on his skull,  and looked tough. Not like the herb or homo I thought he would be. And there he is,  with two runty toy dogs. One of the dogs walked like it had a cucumber up its ass.&#8221;</p>
<p><img data-attachment-id="5658" data-permalink="https://heartiste.wordpress.com/2010/05/12/contrast-is-king/img_2590/" data-orig-file="https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=500&#038;h=500" data-orig-size="1139, 1140" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;3.5&quot;, &quot;credit&quot;:&quot;&quot;, &quot;camera&quot;:&quot;Canon PowerShot SD600&quot;, &quot;caption&quot;:&quot;&quot;, &quot;created_timestamp&quot;:&quot;1273261207&quot;, &quot;copyright&quot;:&quot;&quot;, &quot;focal_length&quot;:&quot;10.093&quot;, &quot;iso&quot;:&quot;3&quot;, &quot;shutter_speed&quot;:&quot;0.01&quot;, &quot;title&quot;:&quot;&quot;}" data-image-title="2590" data-image-description="" data-medium-file="https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=500&#038;h=500?w=300" data-large-file="https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=500&#038;h=500?w=500" class="alignnone size-full wp-image-5658" title="gay toys" alt="" src="https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=500&#038;h=500" width="500" height="500" srcset="https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=500&amp;h=500 500w,  https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=1000&amp;h=1000 1000w,  https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=150&amp;h=150 150w,  https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=300&amp;h=300 300w,  https://heartiste.files.wordpress.com/2010/05/img_2590.jpg?w=768&amp;h=769 768w" sizes="(max-width: 500px) 100vw,  500px" /></p>
<p>This is an excellent example of someone defying expectations. Does anyone doubt this dude gets laid like gangbusters? I bet his idea of a brothel is the local dog park. And he pays in cloyingly cute toy poodle dollars.</p>
<p>I&#8217;ve written before about how important contrast is to your game. Contrast,  like its social dynamics cousins <a href="https://heartiste.wordpress.com/2009/01/29/vulnerability-game/" target="_blank">vulnerability game</a> and <a href="https://heartiste.wordpress.com/2009/03/21/alpha-move-of-the-day/" target="_blank">being unpredictable</a>,  is a status signal of alphaness. When women see a man defy convention,  or wantonly fuck around with societal expectation,  they think &#8220;Oh,  he must be an alpha,  because only an alpha could risk stepping out of line like that.&#8221; Or when they hear a man reveal a potentially status damaging vulnerability at odds with his image of strength,  they think &#8220;He must be really alpha to confess his fear of parrots.&#8221;</p>
<p>No,  seriously,  that&#8217;s the way women think. Subconsciously,  at least.</p>
<p>Contrast game is also a variety of handicap game,  a powerful technique for subcommunicating genetic superiority. Like bright,  heavy plumage on a peacock,  tattoos signal that a man is so genetically fit (and symmetrical) that he can afford the risk to his health and looks that <a href="http://www.scientificamerican.com/article.cfm?id=survival-of-the-tattooed" target="_blank">getting inked with needles will mean for him</a>. Skull tattoo dude in the above photo actually has a double handicap whammy advertising his alpha genetic fitness &#8212; he&#8217;s enduring both the disfigurement of tattoos *and* the public humiliation of walking two gay ass pooches. (I bet he&#8217;s telling the other dude to be careful where he steps.)</p>
<p>How powerful a psychological mindfuck is contrast? Two words:</p>
<p>Susan Boyle.</p>
<p>That ugly broad got on stage and,  in the teeth of a hostile,  pitying audience,  sang the shit out of &#8220;I Dreamed A Dream&#8221;. Result? Standing ovation,  tears flowing like a river,  and eight million copies of her debut album sold in the first six weeks. For a more recent example of the contrast phenomenon,  check out <a href="http://www.zimbio.com/Janey+Cutler/articles/-BupDlV2HBH/Janey+Cutler+Next+Susan+Boyle+VIDEO" target="_blank">this video of Janey Cutler</a>,  the 80 year old singer who elicits the same reaction from an audience expecting something entirely different.</p>
<p>That,  my friends,  is the awesome power of contrast. Now imagine what it can do for your notch count.</p>
<p>So,  you ask,  how do I translate this theme of contrast into practical game advice? I can offer a few suggestions.</p>
<ul>
<li>If you&#8217;re meeting a girl for a dinner after work,  and you&#8217;re in a business suit,  take her to your favorite dive bar or hipster joint after the dinner. She&#8217;ll be pleasantly surprised that a professional such as yourself feels just at home in a dump as in a fancy restaurant. (Note: You really shouldn&#8217;t be taking girls you haven&#8217;t fucked to fancy restaurants.)</li>
<li>Does she think your political views are antiquated? Good. Now take her out to a progressive-oriented art show filled with pseudointellectual revolutionary crackpots. She&#8217;ll start to wonder what else about you she doesn&#8217;t know.</li>
<li>Speak streetwise,  but occasionally drop a big word in your conversation. Intellectual dominance is to smart chicks like physical dominance is to prole chicks.</li>
<li>If you&#8217;re a very masculine man,  peacock with a feminine accessory,  like an ornate bracelet or an earring. If you&#8217;re naturally foppish,  try wearing masculine accessories,  like a big honking watch or combat boots.</li>
<li>Approach a girl like a typical beta,  asking her innocuous questions about how she likes living in the city. Once you have lulled her into an anhedonic stupor,  hit her with a neg. Consider her look of surprise a step closer to intimacy.</li>
<li>Did you meet a girl online and tell her about your starched shirt job? Then show up to the date wearing something boldly stylish. Her mind will race with thoughts of a secret life you&#8217;re hiding from her.</li>
<li>Similarly,  if you&#8217;re a suit-wearing type of guy,  a well-placed tattoo on the inner forearm can do wonders to stir excitement. Just manufacture an excuse to roll up your sleeves,  and watch her eyes light up.</li>
<li>Regale her with adventure stories that are completely at odds with her image of you. For instance,  if you&#8217;re an accountant,  mention the time you spent in the Congo with the little-known aid group Accountants Without Borders,  and how you budgeted the goats for the local village.</li>
<li>Talk about how you voted for George Bush,  then give a buck to a homeless bum you happen to pass by while walking with her. (Alternatively,  you could reverse this sequence if you want to crush the girl&#8217;s hopes. After sucking up to her no-doubt SWPLian worldview,  offhandedly announce after sex how you recently joined the NRA &#8220;to get some shootin&#8217; practice for the big game animals you like to hunt&#8221;.)</li>
</ul>
<p>Contrast is the reason why ugly guys can sometimes do better with women than handsome guys. A handsome man is expected to have his act together in all other ways; in comparison,  nothing much is expected of ugly men. So an ugly man who spits tight game will pleasantly surprise a woman while a good looking man with game will simply confirm what she already believed to be true. And when it comes to making an impression on women,  which man do you think she&#8217;ll remember more? That&#8217;s right,  the man who surprised her out of her lazy thinking.</p>
                                                                                                                            <p>All humans want to be fascinated. Kurt Cobain had it right &#8212; here we are now,  entertain us. Men are entertained by tits,  ass and face. Women are entertained by male charisma and psychosocial savviness. They want to be kept on their toes,  forever wondering what kind of man you are. Defying a woman&#8217;s expectations is the equivalent of a big-boobed woman taking off her sweater and shoving her cleavage in a man&#8217;s face. Her fond memory of you will linger well into the next day.</p>
'


gs20 = epub.EpubHtml(title='Mixing Signals To Dazzle Women',
file_name='mixing_signals_to_dazzle_women.xhtml',
lang='en')
gs20.content='
<h2>Mixing Signals To Dazzle Women</h2>
<p>Mixing your signals &#8212; aka obfuscating your intentions &#8212; is a powerful holistic technique to arouse interest in women,  the class of beings who strangely desire more that which gives the least interest in satisfying their desires.</p>
<p>The status signals (and,  really,  are there any other kind of signals that matter in the least bit when a man is interacting with a woman?) that men display can be broadly categorized into <strong>body language</strong> and <strong>verbal communication</strong>.</p>
<p>Body language comprises a host of nonverbal mannerisms and displays,  from the way a man walks,  to his dress,  his facial expressions,  to how he moves his limbs,  and even to <a href="https://heartiste.wordpress.com/2008/10/15/standing-like-an-alpha/" target="_blank">how he stands</a> or holds a glass. Verbal communication is the words that come out of a man&#8217;s mouth,  and the way in which he says them,  in hopes of creating a desirous spark in an attractive woman.</p>
<p>Most men focus on the words they say,  because the impact of a man&#8217;s body language on women&#8217;s senses is both poorly understood and intangible relative to the impact that he thinks his words carry. Body language is therefore relegated to acting in concert with subconscious feelings of self-worth; for this reason,  body language can be a man&#8217;s worst enemy if he is unaware how his mannerisms betray his hidden emotional state.</p>
<p>Verbal communication is thus overrated and body language underrated by men. The upshot to this formula is that men can chill a bit on the pressure to say the right thing,  if they work to adjust their body language so that it does most of the talking for them.</p>
<p>Mixing signals is the art of telling/showing a woman one thing,  while showing/telling her another. There are four permutations of body language and speech that are possible when approaching women,  only two of which involve mixed signals.</p>
<p><strong>1. Direct Body Language (DBL) + Direct Verbal Communication (DVC)</strong></p>
<p>You make a bold statement of intention with both your body motions and your words. Example:</p>
<p>Walking slowly toward a woman,  holding eye contact the whole way,  stopping in front of her,  <a href="https://heartiste.wordpress.com/2012/08/03/pregnant-pause-game/" target="_blank">pausing for effect</a>,  and with a low,  deliberate tone of voice,  saying,  &#8220;I&#8217;d regret it forever if I didn&#8217;t come over and see if you are the type of woman I want to get to know better.&#8221;</p>
<p><strong>2. Indirect Body Language (IBL) + Indirect Verbal Communication (IVC)</strong></p>
<p>You engage a girl with a seemingly innocuous statement about some peculiarity in your shared environment,  and comport yourself like you have another place to be and she just happens to be there to listen to you. Example:</p>
<p>Looking over your shoulder at the girl,  turning your body to partially face her,  one foot pointed in another direction,  rocking back on your heels as you speak,  glancing once or twice at some faraway object,  and with a neutral tone of voice,  saying &#8220;If the bookstore weren&#8217;t so full of poseurs,  we might have a chance to get a book within the next hour.&#8221;</p>
<p><strong>3. DBL + IVC</strong></p>
<p>You make a bold statement of romantic intention with your body and facial expressions,  while speaking neutrally so as to suggest you are not interested in hitting on her. Example:</p>
<p>Directly facing the woman,  positioning yourself so that eye contact is unavoidable and escape is limited,  occupying her personal space,  you ask in an unthreatening,  bland tone of voice,  after a mood-heightening silent pause,  if she can direct you to the nearest toy shop so you can buy a gift for your niece.</p>
<p><strong>4. IBL + DVC</strong></p>
<p>You verbally communicate your romantic interest while your body language bespeaks disinterest. Example:</p>
<p>Body rocking,  feet positioned as if you are about to walk off,  approaching at an angle with shoulders turned halfway outward,  eyes surveying your environment,  you open her directly with a strong sexual vibe that belies your mannerisms.</p>
<p>Which of these styles of interaction is best? That&#8217;s hard to say,  because the style that works best depends in some measure on the skill of the womanizer. A sexually needy man who experiences bouts of nerves when cute girls are near stands a good chance of being perceived as incongruent in his words and behavior if he tries to directly open a girl while comporting himself as if he&#8217;s too cool for school. Similarly,  an experienced player with rock solid confident body language who masks his intentions under a flurry of misdirecting banalities may strike a girl as a coward who is too skittish to say what&#8217;s on his mind.</p>
<p>However,  this contextual problem aside,  I believe a useful generalization about the effectiveness of the different approach styles can be made.</p>
<p><a href="https://heartiste.wordpress.com/2012/11/29/indirect-vs-direct-vs-clever-openers-which-is-best/#comment-391142" target="_blank">Eric Disco</a> comments:</p>
<blockquote><p>This is essentially what most guys do when they attempt to be indirect,  they are indirect with their words (“How do you get to Starbucks?”) but then they are very direct with their body language–mainly eye contact and body orientation. They face her and give her lots of eye contact,  looking at her continuously,  as if they’ve just spotted a rare bird. From my experience,  instead of combining the best of both worlds,  this combines the worst.</p>
<p>When you’re direct,  it shows balls. The drawback is that you are betraying a lot of interest,  which lowers your value and makes you seem like less of a challenge. When you combine an indirect verbal opener with direct body language,  you betray interest but don’t show any balls at all.</p>
<p>Once you’re in the interaction with her,  you can start to show more interest physically,  once she’s earned it. You can be more sexual with your eye contact,  etc. But if you’re going to open indirect,  then be indirect. Don’t betray too much interest. Act like she just happened to be there and so you said something to her. If you’re going to walk across a room/park just to talk to her,  then show some balls. Go direct.</p></blockquote>
<p>Eric is onto something. The DBL + IVC style is probably the riskiest strategy for the average man to pull off. It&#8217;s too easy to come across like a suave dude who can&#8217;t go the extra distance and just ask the girl out. I bet a lot of you good-looking guys who read this blog have this problem.</p>
<p>Any kind of situation which necessarily calls for a direct approach &#8212; say,  walking across a park or large room in full view of your target so that she is under no illusion why you are moving in on her &#8212; would benefit from a direct style verbal opener. You can still go indirect in these circumstances,  but you had better be a master at manipulating women&#8217;s expectations so that your value remains at a constant high level compared to them.</p>
<p>Men new to the stealthy art of seduction are best served learning pickup by employing the IBL + IVC style. This is,  in fact,  what most pickup artists teach their acolytes. The typical woman <a href="https://heartiste.wordpress.com/2012/11/29/indirect-vs-direct-vs-clever-openers-which-is-best/" target="_blank">prefers the indirect approach</a> from the typical man,  and the inexperienced man is not going to possess the degree of self-amused state control that is required to successfully pull off direct approaches. The newb will need gradual indicators of interest from women to build up his confidence levels to a point where he is comfortable risking more on direct openers and interactions of powerful sexual intention.</p>
<p>Then,  too,  the newb can get a better grasp of gauging a woman&#8217;s &#8220;buying temperature&#8221; by adjusting his body language from indirect to direct and back to indirect,  as opposed to the more difficult route of direct to indirect back to direct. It&#8217;s easier to maintain plausible deniability with the former than with the latter.</p>
<p>So,  I&#8217;d say IBL + IVC is optimal for younger men and less experienced men. This is not a mixed signal strategy at the outset,  but it can be farther along in the process when it is simpler to incorporate different verbal and nonverbal tactics.</p>
<p>Where it gets interesting is the IBL + DVC strategy. This can potentially be the most powerful approach technique wielded in the right hands. Such a man is perceived as having the conviction of his words,  but simultaneously sending barely perceptible signals that his interest level is waning,  or that he&#8217;s hard to keep engaged. Naturals tend to this style,  and the classic archetype is the devil-may-care badboy who speaks of lustful things to a girl while his eyes wander around the room scanning for fresh meat.</p>
<p>Generally,  though,  mixing signals is a technique best left for experts. The risk of mood-killing incongruence is very high,  and I&#8217;ve seen far too many enthusiastic men muck it up when they couldn&#8217;t sufficiently manage the inherent discrepancy between their words and their mannerisms.</p>
<p>YaReally makes the <a href="https://heartiste.wordpress.com/2012/11/29/indirect-vs-direct-vs-clever-openers-which-is-best/#comment-391104" target="_blank">inarguable point</a> that,  once a certain level of inner confidence is achieved,  it doesn&#8217;t really matter what kind of approach style a man uses.</p>
<blockquote><p>The PUA community used to think you needed solid indirect openers to open. Then we found out you could go direct. [&#8230;]</p>
<p>Now we understand that you can open with anything,  as long as what you open with comes from a place of self-amusement and congruency.</p>
<p>When you think “How should I open this girl?” you’re essentially thinking “What can I say/do to earn this girl’s validation?” and you’re already coming from a frame of having lower value than her.</p>
<p>When you think “What I’m saying is gold,  of course she’ll love me,  I’m so awesome!” you’re essentially screening her for “Is she cool enough for me to let her hang with me?” and you’re coming from a frame of having higher value than her.</p>
<p>Girls generally pick up on this subconsciously,  because they’ve spent their lives having to learn to quickly assess “is this person being genuine/honest with me or are they trying to get something from me?”</p>
<p>A lot of why “Who lies more?” worked so well was because the guys learning it felt like they found the secret invincible formula,  so when they approached with it they were approaching from that “This is going to blow her mind,  of course she’s going to love me” frame.</p>
<p>Direct worked because the guys who tried it were sick of going indirect and beating around the bush and wanted to just get their intentions out in the open so they were just saying “HEY. You’re cute,  I’d kick myself if I didn’t come say hi.” and expecting it to work,  so it did.</p></blockquote>
<p>Some of you may be asking,  &#8220;Doesn&#8217;t YaReally&#8217;s advice contradict the study you just posted about how indirect,  innocuous openers are best?&#8221;</p>
<p>Good question! Superficially,  yes. But you&#8217;ve got to understand that most of the men involved in these studies have no game,  have never heard of game,  and likely wouldn&#8217;t understand the concept of congruence if you whacked them over the head with it. These studies examine the responses of women to the behavior of the *average,  no-game-having* man,  and in that context,  indirect is best. Since that context is most contexts,  it is good advice to follow for most men. Men who have been exposed to a new way of thinking about women and seduction are better equipped to pursue different approach strategies that streamline the process and maximize their lay rates.</p>
'

gs21 = epub.EpubHtml(title='trump-up charges',
file_name='trump-up_charges.xhtml',
lang='en')
gs21.content='
<h2>Trump-Up Charges</h2>
<p>Women love to bitch and moan about their men. It&#8217;s in their blood. But it matters not,  most of the time. As long as you smite her heart with your heraldic war pike of forged steel alphaness,  her bitching and moaning will waft into the ether,  having no influence whatsoever on her desire to cling to you. In fact,  bitching and moaning is often a sign that the woman is deeply in love,  for such a powerfully debilitating emotion ushers forth a fusillade of half-hearted complaints as a grounding mechanism to steady her so that she can make at least semi-cogent rationalizations why she can&#8217;t get enough of your assholery.</p>
<p>There is,  however,  a time and context when the complaints carry more weight. This is usually right near the end of a relationship,  when she has already checked out and is now trying to wriggle free without confronting the real reasons why she feels no tingle. You will know this is happening because complaints you rarely heard before suddenly come out of nowhere,  and with increasing frequency. Her bitching,  too,  will take on a serious cast,  and the playfulness with which she needled you before will be gone,  replaced by a somber recounting of grievous faults. You will almost picture her wearing a green eyeshade as she ticks off your bothersome habits that,  for reasons unclear to your formulaically analytical male mind,  she finds irredeemably annoying what once she thought charming,  and evidence that you are unsalvageable as a boyfriend.</p>
<p>&#8220;You&#8217;re late all the time.&#8221;</p>
<p>&#8220;I hate they way you kiss with the side of your lips.&#8221;</p>
<p>&#8220;You never got me anything nice.&#8221; (You&#8217;ll notice girls using an out-of-place past tense when you have been mentally demoted to ex-lover.)</p>
<p>We here at the Chateau know the reason why she has morphed into a human resources department assistant manager: you lost your alpha mojo. Her complaints,  more often than not utterly baseless trumped-up charges,  are simply mediums through which she contextualizes your emerging betatude. She cannot fathom the subtleties of character deficiency and behavioral emasculation that turn her off,  but she can wrap her frazzled hamster around the one time you were ten minutes late picking her up from the train station. And since a woman&#8217;s memory for trivial details rivals a quad core CPU,  you can expect that she will remember retroactive annoyances from five years ago that today serve as convenient nitpick fodder to justify the torrent of hypergamous preprogramming that propels her away from your domesticated ass.</p>
<p>Happily for you readers,  the Chateau is a one stop shop for all your relationship management needs. We don&#8217;t just diagnose the problem; we give you solutions. So what do you do when the end is nigh and the bitching has evolved into a stone cold staff meeting? Whatever you do&#8230;</p>
<p>DON&#8217;T ENGAGE HER LOGICALLY.</p>
<p>Women are probably capable of some rudimentary logical thinking in a pinch,  but it isn&#8217;t their default mental algorithm,  and they won&#8217;t like having to be logical when they could defer to their insanely precocious <em>feeeeelings</em> instead. So when you engage a woman logically,  assaulting her with the facts and bolstering your case,  you are actually signing your own notice of dismissal. In the court of love,  fairness is a fleeting proclamation and evidence an obstacle to be tampered with on the way to the Siberian celibacy camps.</p>
<p>&#8220;You&#8217;re late all the time.&#8221;</p>
<p>&#8220;No,  I&#8217;m not. Once or twice,  maybe. But do you remember me being on time for the house party last week?&#8221;</p>
<p>BAD.</p>
<p>&#8220;You&#8217;re late all the time.&#8221;</p>
<p>&#8220;You would be too if your ten other girlfriends were constantly bugging you.&#8221;</p>
<p>GOOD.</p>
<p>&#8220;I hate the way you kiss with the side of your lips.&#8221;</p>
<p>&#8220;I don&#8217;t do that. You&#8217;re just making shit up.&#8221;</p>
<p>BAD.</p>
<p>&#8220;I hate the way you kiss with the side of your lips.&#8221;</p>
<p>&#8220;Next time I&#8217;ll aim for your ear.&#8221;</p>
<p>GOOD.</p>
<p>&#8220;You never got me anything nice.&#8221;</p>
<p>&#8220;Sure I did. What about that cashmere sweater I got you for your birthday?&#8221;</p>
<p>BAD.</p>
<p>&#8220;You never got me anything nice.&#8221;</p>
<p>&#8220;Fuck you. That <a href="https://heartiste.wordpress.com/2009/05/19/be-a-skittles-man/" target="_blank">bag of Skittles</a> cost me an arm and a leg.&#8221;</p>
<p>MOST EXCELLENT.</p>
<p>The above are merely suggestions for dealing with the red flags of rationalization bitching. <a href="https://heartiste.wordpress.com/2009/08/13/relationship-game-week-agree-and-amplify/" target="_blank">Many game strategies</a> are available to you,  and all are good in their own way. The point of this post is that under no circumstances should you ever <a href="https://heartiste.wordpress.com/2008/12/05/dirty-photo-album/" target="_blank">take a woman seriously</a> in relationship matters,  unless she is waving a small white stick with a pink tip in front of you.</p>
<p>Even then,  <a href="https://heartiste.wordpress.com/2009/03/17/predator-sluts/" target="_blank">proceed with caution</a>.</p>
'

gs22 = epub.EpubHtml(title='kiss',
file_name='kiss',
lang='en')
gs22.content='
<h2>When To Move On For The Kiss On The First Date</h2>
ft writes:</p>
<blockquote><p>I&#8217;d like your thoughts on a recent date I had.</p>
<p>We were introduced through family. <strong>[Ed: Never a good idea if you play the short game.] </strong>We went on one date and it went well. Started 10 PM and didn&#8217;t end until 530AM.</p>
<p>Conversation was free and easy and I escalated slowly throughout the evening,  although I didn&#8217;t push hard enough. When I needed to demonstrate value I did.  When I told her to follow she obeyed. I dropped some good negs.  I had problems with my ATM card but she had no problem paying until I straightened them out (we visited 4-5 venues) without a fuss. We said our goodbyes.</p>
<p>The second date is the one I&#8217;d like you to comment on.  It was the next day and I called her and invited her out for drinks.  She told me she&#8217;d call me after dinner and kept her word.  She sounded surprised to hear from me so soon but didn&#8217;t hem or haw and we met within a half hour.  This time we found a pool hall and I displayed my superiority while gently negging her.</p>
<p>HER: Am I really the worst pool player you&#8217;ve ever seen?</p>
<p>ME: It&#8217;s kind of tough to call.  I knew this blind guy who liked to play&#8230;</p>
<p>She liked that one.</p>
<p>We moved to a lounge which had couches and single chairs. I guided her to a loveseat and she didn&#8217;t protest.</p>
<p>I spread out alpha style and put my arm up on the back,  almost around her.  We chatted for a while,  light touching,  teasing.  She went to the bathroom and this is when the shit test started. I hadn&#8217;t had a real one so far that night or on the first date.</p>
<p>I noticed that after she returned from the bathroom another button on her shirt was undone and her hair was a little more tousled than before.  She began by complementing my overall physique,  but she then started to ask why I wore my clothes a little more loosely than usual. I told her it was for comfort. She told me she couldn&#8217;t tell whether or not I was in shape.  As I was wearing a polo and an undershirt she said she could better judge if I removed the polo.</p>
<p>Let me say that a year ago I might have complied to a request like this without hesitating,  but after some game research and restoring my manly dignity,  I do not perform for women,  nor do I give something for nothing. Nor would I be embarassed about what she would see. I don&#8217;t have a six pack but I&#8217;m tall,  lean,  with wide shoulders and v-shaped back.</p>
<p>I decided to see if she would put her money where her mouth was and told her if she wanted it she would have to kiss me. She said no. Right then I knew it was about control. If she had wanted an excuse to escalate she had it. I reframed by teasing her she didn&#8217;t impress me with her sales skills (she&#8217;s in sales). That bought me time to pay<br />
and walk her out of the bar and home. It was about a forty minute walk. We had a good convo pretending to bargain over the price to see me without the outershirt.</p>
<p>Halfway to her place I asked her if she could do me a favor. I took off my jacket and tossed it to her. &#8220;Can you hold this for me? I&#8217;m warm.&#8221; The smile on her face was priceless. She thought she was about to get what she wanted. A few minutes later when handing me back the jacket,  she made an attempt to lift up my shirt. I gently stopped her hands and feigned disappointment that she would resort to trickery.  The rest of the walk home I kept about half a step ahead.</p>
<p>As we reached her door I slowed but didn&#8217;t stop and said my goodbyes as I turned to continue home.  She looked stunned that I didn&#8217;t hug her or peck her on the cheek. It was cordial but minimal with no contact.</p>
<p>As I walked away I was proud of myself for not selling out to desperation. My gut told me following an order for her would have spelled doom,  but I know I missed an opportunity somewhere. Would she say yes to another date?</p>
<p>Appreciated, <br />
Shaft</p></blockquote>
<p>Even though this question from the reader is about his second date,  the title of the post is about moving in for the kiss on the first date,  since it is the first date when you should get physical with a girl. The majority of kiss-less first dates lead nowhere. It is also a bad idea to schedule a second date the very next day following the first date. This reader was one of the fortunate few to dodge some self-inflicted seduction-killing obstacles. The rest of his game &#8212; such as the handling of her shit tests &#8212; was good,  and probably accounted for her continued interest.</p>
<p>Her are some basic rules about kissing on the first date:</p>
<ol>
<li><strong>Do not kiss her when you meet her at the start of the first date.</strong> You are not as debonair or as European as you think you are,  and neither is she. A kiss upon meeting is going to feel awkward for her and for you. This goes even in those first date cases where you previously had a sloppy make-out with her in the bar on the night when you scored her digits. Actually,  it goes doubly for those instances. (Previous sloppy bar make-outs reveal your hand,  so your job should be to temporarily disqualify yourself so she doesn&#8217;t think you are too easy.)</li>
<li><strong>Do not kiss her at the end of the first date unless there was significant physical contact during the date.</strong> Multiply the awkwardness of the initial meeting kiss by ten and you will know the feeling of planting a night-ending wet one on a girl at the end of a date that was woefully free of any physical connection.</li>
<li><strong>Do not attempt to force a nonexistent rapport by kissing the girl.</strong> This rule applies for any date,  but its disregard is most evident on the first date. Many men will try to light a fuse in their dates by moving in for the kiss sans any physical groundwork,  incorrectly thinking that their shared sterling,  intellectual conversation was proof enough that she was ready for kissing. They are then flummoxed when she delivers the cheek turn,  the &#8220;whoa,  not so fast&#8221; rejoinder,  or,  worse,  the &#8220;what do you think you&#8217;re doing?&#8221; lawyerspeak shut-down. Instead of the smooth move these men imagined in their heads it would be,  they end up lurching clumsily from chit chat at a four foot distance to a lips-probing kiss flying in at the speed of light. Kissing is an emergent property of successfully executed game; it is not a standalone game maneuver that you can run in any context. If you haven&#8217;t escalated physical touching with a girl during a date,  don&#8217;t think that a kiss after three hours of arms-crossed shop talk will advance the seduction.</li>
<li><strong>Do not go for the first date kiss in a crowded room</strong>. <a href="https://heartiste.wordpress.com/2008/01/13/best-feeling-in-the-world/" target="_blank">Venue bounce</a>,  drink,  venue bounce again,  settle into a sofa at a lounge,  make out. Most girls lie to themselves that they are &#8220;not that kind of girl&#8221;; why give a girl an excuse to test her self-delusions by moving in for the kiss where a <a href="https://heartiste.wordpress.com/2008/05/05/pda-is-beta/" target="_blank">huge crowd can analyze the depravity of her sluttiness</a>?</li>
<li><strong>The ideal first date kiss should happen sometime in the middle of the date.</strong> Kino escalation,  growing intimacy,  then kissing,  followed by a cooling off push-away,  more light banter,  reinitiated kino,  etc&#8230; if you can physically peak in the middle to last third of the date,  you will leave her wanting more while simultaneously avoiding the dreaded last minute kiss of desperation that poisons so many dates. Mid-date physical peaking also prevents ASD (anti-slut defense).</li>
</ol>
<p>So to sum up,  don&#8217;t kiss at the very beginning or the desperate end of a first date,  don&#8217;t force a kiss if she isn&#8217;t giving indicators of interest,  escalate physical contact until you ideally begin kissing her in the middle to last third of a date,  and wait to kiss her when you&#8217;re settled into an intimate location (this includes a back alley if the weather is warm).</p>
<p>Caveat: If you are going for a bust-or-bail first date same night lay,  kiss her whenever the fuck you feel like it. An end-of-official-date kiss is simply a prelude to a beginning-of-unofficial-date night of fornication.</p>
<p>The ideal kiss window should <a href="https://heartiste.wordpress.com/2008/08/04/kiss-close-in-front-of-her-friends/" target="_blank">open effortlessly if your game is tight</a>. Girls who are being seduced properly *want* to be kissed. Always check for dilating pupils,  hair twisting,  leg opening,  lip licking,  heel dangling,  head cocking,  bar stool swiveling,  drink swilling,  incidental thigh touching,  and hand on chin head propping.</p>
<p>To the reader: it&#8217;s hard to know if she&#8217;ll agree to a third date based on how you described the second date ending. It looks like you fell into the trap of <a href="https://heartiste.wordpress.com/2010/07/26/overgaming/" target="_blank">overgaming</a> to compensate for some fuck-ups you may have done on the first date,  and to reestablish hand after she denied you the kiss when you playfully challenged her to one. In your zeal to demonstrate non-neediness,  you forgot that you have to make a physical move on a girl to get the ball rolling toward sex. There is a fine line between slyly camouflaging your intentions and showing no intention at all. Two dates have now gone by without any kissing or intimate touching,  from what you have written. This is a recipe for a seduction about to fizzle.</p>
<p>What you did by nonchalantly walking off was probably better than ending the date on an awkward goodnight cheek kiss where she held all the cards,  but you shouldn&#8217;t have put yourself in that situation to begin with. Had you prepped the courtship by kissing her earlier in the evening (let&#8217;s say during drinks at the lounge),  the date-ending goodbye would not have been a test of wills pitting your aloofness against her coyness. Sure,  by unexpectedly denying her the long-awaited goodbye kiss of prostration you may have won the battle,  but you lost the war well before your tepid final flanking maneuver.</p>
<p>In the future,  push for kissing by the middle of the first date,  but don&#8217;t overdo it. Making out with a girl for too long and too hard on the first date &#8212; again,  unless you are gunning for a SNL &#8212; will gradually lower your value and,  hence,  raise her buyer&#8217;s remorse,  leading to <a href="https://heartiste.wordpress.com/2007/05/22/flake-odds-point-system/" target="_blank">flaking on subsequent dates</a>. The perfect seduction moves two steps forward,  one step back. No kissing = celibate LJBF. Too much kissing = flaking. Ideal kissing = mid-date,  in measured doses. You want to break the lip barrier without making a spectacle of your horniness.</p>
<p>Always remember that the alpha male demonstrates by his actions complete mastery over his sexual desire,  and knows when and how to parcel it. A man with simmering,  feral arousal that he can control is intoxicating to women. This is why make-outs followed abruptly by takeaways or teasing push-offs is so attractive to women &#8212; they love that they can&#8217;t figure out how much you really want to fuck them.</p>
<p>When you kiss on the first date,  stop before she does,  lean back to talk some more,  and chastise her lightly for moving too fast. Repeat a couple times during the night,  then hold her hand as you walk her home. Kiss her *before* you get to her door,  then drop her off about twenty feet from her place (to reduce the impression of formality that surrounds a door-step departure),  giving her a hug if you wish. Then tell her you had a great time AND LEAVE. Do not tell her you&#8217;ll call her,  or try to set up a second date. Just leave,  and she&#8217;ll thank you later,  in the best way women know,  for blessing her happily restless sleep that night with the inscrutability of your actions.</p>
'

gs23 = epub.EpubHtml(title='get lost',
file_name='get_lost.xhtml',
lang='en')
gs23.content='
<h2>Get Lost</h2>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Most girls avoid inciting confrontation. But some girls are constitutionally nasty. All girls can occasionally be nasty if they are pushed hard enough (or PMSing hard enough). American girls are <a href="https://heartiste.wordpress.com/2009/06/15/the-masculinization-of-the-western-white-female/" target="_blank">getting manlier</a> and,  hence,  nastier,  so the occasions you will encounter nastiness from a girl in America and her Western satellites are likely increasing in frequency.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Some things a nasty bitch will utter are so grating you feel impelled to haul back and send her to the moon. &#8220;Get lost&#8221; is one of those things. Of course,  you don&#8217;t want to do this. Not only will it result in a white knight brigade gang-tackling you in hopes of receiving a pat on the back from some fat hog in flip-flops,  it will kill your pickup momentum.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>The best answer to female nastiness is calm. As long as your demeanor is calm and you look unflustered,  you will knock a nasty cunt off her game plan. She&#8217;s expecting one reaction; you&#8217;re giving her another.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Calmness is essentially non-reactiveness. When you react,  you accede,  implicitly or explicitly,  to your antagonist&#8217;s frame. When you react,  you confess defensive insecurity,  even if objectively you are not,  because perception is all that matters in seduction. Defensiveness is the biggest game-killer,  outside of supplication. If you ever observe naturals or experienced players hitting on women,  one thing you&#8217;ll notice they all have in common is a complete and total lack of defensiveness or supplication. The non-neediness and self-certainty of the inveterate player are so ingrained that he couldn&#8217;t be otherwise if he tried.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>So,  to sum up,  when you encounter shocking nastiness from a girl:</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>1. Stay calm<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                            2. Don&#8217;t react<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                            3. Announce your preferred intention</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Number 1 is very hard to do if you are a young man full of impulsivity and heavy balls. But it comes with practice. Hot emotions can be corralled and channeled,  just like yogis can train themselves to focus inwardly and feel less pain.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Number 2 can be mastered simply by willing yourself to pause for a second or two in mental silence before responding to a girl who has attempted to get under your skin. The <a href="https://heartiste.wordpress.com/2012/08/03/pregnant-pause-game/" target="_blank">pause of alphaness</a> is a powerful technique,  and will help you gather your thoughts and keep a poker face. It is also very unsettling to your opponent.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Number 3 is reframing. This is where you apply the proper tension with the words you choose to relay to her. A substitution of her tacit demands with your alternative preference implies your indifference and perhaps mild annoyance. You are not angry or spiteful. You are condescending.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>So,  for example,  a girl says this to you:</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>&#8220;Get lost.&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>You would ideally respond with this:</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>&#8220;No,  I think I&#8217;ll stay right here.&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>No anger,  no spite,  no sulking,  no defensive flailing. Just a calm iteration of fact and an imposition of your will on the world,  wrapped in an unmovable frame.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>If she really hates you,  she&#8217;ll mutter something like &#8220;fuck you&#8221; under her breath and walk off,  which is the equivalent of taking her ball home and declaring victory. But the perception will be that you will have won,  standing your ground like an unflappable mofo. A small measure of self-satisfaction will materialize in a smirk on your face. It&#8217;s these little victories that add up to a rich,  fulfilling life.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>If she doesn&#8217;t really hate you,  and was just being bitchy because bitch,  her reaction will be an amalgam of surprise,  indignation and intrigue. All these reactions are better than the alternative,  because they all mean her frame has been broken and subsumed into yours. Great love often germinates in such difficult soil.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Now I know some of you are incredulously asking yourselves,  &#8220;So an alpha male is never supposed to get angry,  even when such anger is fully justified?&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>No,  I didn&#8217;t say that. An alpha male should favor being proactive over reactive. What this means in practice is that anger is best displayed intermittently,  infrequently,  and unexpectedly. It is also best used when its usage is personally advantageous. The rules of the sexual market are not guided by principles of fairness; an angry defensive outburst moves you no closer to your goal of pleasure,  and usually moves you further from it.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Bitchiness should be answered first with bemused calm,  which steals the bitch&#8217;s thunder and robs her of the satisfaction of provoking the expected butthurt response. Preternatural calm and steadfast state control will induce in the bitch complacency,  guard-lowering,  and second thoughts,  from which a seduction may move forward,  or from which you may lower the war hammer of ego smiting. Give the bitch room to bitch,  implant in her the impression that you aren&#8217;t easily provoked and might even be worth getting to know,  and then,  when she least expects it,  reveal the awesome glory of your disgust with her as a person.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                            <p>Dishing out unforeseen comeuppance is almost as satisfying as sex. But it&#8217;s a long game,  for those who have the patience and discipline to master not only the egos of others,  but one&#8217;s own ego.</p>
'


gs24 = epub.EpubHtml(title='femme fatales',
file_name='femme_fatales.xhtml',
lang='en')
gs23.content='
<h2>How To Handle Femme Fatales</h2>
<p><a href="http://aliasclio.blogspot.com/" target="_blank">Clio</a> wrote an informative and entertaining series of posts about the taxonomy of femmes fatales &#8212; those irresistible women who will do a man no good if he leaves himself ignorant of and defenseless to their machinations. I&#8217;ve decided to do a counterpost explaining to men how to guard themselves against the four main femme fatale types as described by Clio,  based on my experiences with women who fell into one or the other category.</p>
<p><a href="http://aliasclio.blogspot.com/2008/07/heartbreakers-5-gold-digger.html" target="_blank"><strong>The Golddigger</strong></a></p>
<blockquote><p>The gold-digger is the classic female heartbreaker,  the one everyone except a few feminists loves to hate. She is not a prostitute: although she marries for money she does not have sex for money. [&#8230;]</p>
                                                                                                                                                                                                                     <p>In fact,  the chief characteristic of this type of female heartbreaker is her ruthlessness in pursuit of what she wants. She has to be careful not to fall in love,  because it would cloud her judgment and because the type of man she requires is likely to be frightened by displays of emotional desperation and put off by neediness.</p></blockquote>
                                                                                                                                                                                                                     <p>While the golddigger&#8217;s ultimate goal is marriage to a wealthy man,  she will have sex with rich guys as long as the trinkets and baubles flow. Because payment for her services is not so direct,  often coming days or weeks later instead of being left on the endtable by the bed,  she is able to delude herself into believing she is not a common whore. But absent love,  she is ideologically indistinguishable from her streetwalker cousins. She&#8217;s simply smart enough to secure payment without a pimp middleman,  and to do it from one or two smitten sources instead of a carousel of johns.</p>
                                                                                                                                                                                                                     <p>The way to handle a golddigger is to establish your terms of courtship early on,  before she has had a chance to suck you into her reality. You really want to sniff out the golddigger quickly,  because if you don&#8217;t have the money,  or you do have the money but don&#8217;t want to buy a woman&#8217;s love with it,  then you&#8217;ll want to waste as little time dating golddiggers as possible. Without game,  you&#8217;ll never change them. The good news is that it&#8217;s a simple matter tricking a golddigger to reveal her true inner whore.</p>
                                                                                                                                                                                                                     <p>The secret is this: Golddiggers target wealthy but gameless greater betas and alphas who deal with women in a very traditional and conventional manner &#8212; i.e. buying her drinks and taking her to fancy dinners on the first date. These are the kind of men who work all their lives to eventually purchase arm candy they can bring to cocktail parties. You can jolt the golddigger right out of her utilitarian programming by QUALIFYING HER. For example,  you must make clear early on you don&#8217;t buy drinks for women and,  in fact,  if she&#8217;s cool,  you&#8217;ll let her buy a drink for you. Another effective tactic for exposing the golddigger and putting her on the hot seat is to remark on her good taste in clothes or jewelry (golddiggers love when you share their materialistic worldview) and then say without a hint of irony that it&#8217;s a good thing you dressed up for the occasion and wore your best watch &#8212; while pointing to the Swatch on your wrist. If she laughs or compliments your watch,  you have a shot to convert her. If she takes you seriously and looks around the room annoyed or cackles sarcastically,  you can escape on a &#8220;bathroom break&#8221; and leave her with the check.</p>
                                                                                                                                                                                                                     <p>The golddigger is not used to the tables being turned like this. Indignantly,  she will either leave in a huff or become surprisingly intrigued by your chutzpa. You win no matter which path she chooses. She leaves; you&#8217;ve now avoided spending money on a <em>de facto</em> whore without the integrity to put out <em>quid pro quo</em> on the first date like an actual whore. She stays; you have broken her and ensured her attraction for you will be genuine.</p>
                                                                                                                                                                                                                     <p>The more ruthless the woman,  the bolder <strong>and more alpha</strong> you have to be in your dealings with her. An attractive and successful golddigger &#8212; and they are usually 8s and up; less attractive golddigger wannabes are simply not in the field of view of rich men &#8212; requires the utmost boldness. Beta nerds who have made a lot of money in the tech field should not attempt to tangle with them. They will be chewed up and left more misogynistic than they were before they met her.</p>
                                                                                                                                                                                                                     <p>The only time it is acceptable to play by a golddigger&#8217;s rules is when you don&#8217;t mind spending the money for access to sex with a hotter women than you could normally acquire relying on just your personality and charm. There are many men like this,  so the golddigger is here to stay. I estimate their numbers in the general population of bangable women at around 15%.</p>
                                                                                                                                                                                                                     <p>One thing you have to remember about golddiggers &#8212; they are not that smart. Don&#8217;t confuse ruthlessness for smarts. Being base,  corporeally-centered creatures with a crass understanding of the sexual market,  they are easily manipulated into behaving by the standards you set for them as long as your game is tight. Shock and awe is how I would describe the game you need to break their will.</p>
                                                                                                                                                                                                                     <p>Btw,  it is possible for a golddigger to fall in love with a man based solely on his money. Cash is a form of power,  and women are universally attracted to male power in whichever form it comes. Beware: If she fell in love with you for your money,  she&#8217;ll fall out of love with you twice as fast if the money disappears. Hopefully for you,  by that time,  she&#8217;ll be a has-been cougar and have no options but to deal with your gameless,  poor ass.</p>
                                                                                                                                                                                                                     <p><strong><a href="http://aliasclio.blogspot.com/2008/07/heartbreakers-5-waifneurotic-revised.html" target="_blank">The Waif/Neurotic</a></strong></p>
                                                                                                                                                                                                                     <blockquote><p>There is the more vocal Neurotic type,  who is probably very intelligent and a high achiever (think Plath,  left,  or Wurtzel,  bottom left,  both excellent students),  who probably suffers from depression and will do her best to ensure that you do as well; and there is the Waif,  who is more obviously fragile in appearance than the neurotic,  less verbal,  less likely to be an academic success,  and more drawn to the visual arts than to writing. What they have in common is that they suffer,  and use their pain to hold on to their men. [&#8230;]</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Forget worrying about gold-diggers,  men. It&#8217;s these ladies who will find a way to make you miserable every time. The ones on the Neurotic end of the spectrum will wear you out trying to take care of them when they&#8217;re sick; worry you to death with threats of suicide; make an idiot of you as you try to amuse them with silly jokes or make them feel loved with romantic gestures; persuade you spend all your time and money trying to make them happy. None of it will ever be enough. And then they will leave you for someone else,  or have to go for drug or alcohol treatment,  or decide that they need to be on their own for a little while.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>The Waifs won&#8217;t expect you to spend much money,  and they tend not to demand as much attention as Neurotics,  but if annoyed with you they will give you the silent treatment,  drifting around sadly with huge eyes,  attracting other men,  and suddenly leave you for one. Like Neurotic heartbreakers,  Waifs tend to develop drug or alcohol problems,  but theirs may be more serious,  as they don&#8217;t have the same level of self-discipline as their Neurotic sisters. They won&#8217;t threaten suicide verbally,  but you might come home to find one of them half-dead from an overdose. Lots of drama with these women. [&#8230;]</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>One caution I want to make is that not all Neurotic or Waif women are heartbreakers. It&#8217;s a special type of Neurotic or Waif who is also a <em>fatale</em>,  who learns to use sexual conquest as a temporary antidote to unhappiness.</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>We all know these types &#8212; think any role played by Winona Ryder or Gwyneth Paltrow. I agree with Clio,  these women are more dangerous than golddiggers because they wield their feminine power with subtlety and innocent sincerity. Their coin of the realm is fragile femininity and emotional manipulation,  as opposed to sex for resources barter. If you are a man who likes his girls girly,  you won&#8217;t know what hit you until it&#8217;s too late and you&#8217;re in with both feet and all your heart.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>The only way to learn to deal with the waif and neurotic is through experience. It&#8217;s hard to teach a man to temper his protective instinct. A waif who connects with a man&#8217;s heart and pride enslaves him more than the golddigger who connects through his loins and wallet.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>The solution to the emotionally manipulative waif/neurotic is to <strong>call her bluff</strong>. I once had a girl threaten to kill herself as she sat on the edge of my bed,  spastically emptying desk draws for bottles of pills she could swallow. The normal man would crumble and attempt to alleviate her pain and tears with his comfort and listening ability. WRONG. This will only embolden her to greater future outbursts. Instead,  I opened the window and told her to jump,  it&#8217;ll get the job done faster. It worked. She cursed and stormed out,  only to return,  humbled,  a couple days later.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Warning: Sometimes she will actually go through with it and kill herself. Be strong. Her mental weakness is not your moral crisis. You have just saved yourself years of heartache dealing with her recurrent emotional breakdowns.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Don&#8217;t get caught up in the waif&#8217;s exploitative exhibitions. <a href="https://heartiste.wordpress.com/2008/07/08/the-sixteen-commandments-of-poon/" target="_blank">You are the oak tree</a>,  strong and rooted. Let her flail away; you are immoveable. When she sees her tawdry drama and passive-aggressiveness is having no effect on you,  she&#8217;ll fall deeper in love. Remind her in the strongest terms that her happiness depends on herself,  not you. Tell her that she must understand her low self-esteem is no excuse for her shitty behavior and you have little patience for it. You will not be there to validate her ego. Flirt ostentatiously with other women so she knows you can leave at a moment&#8217;s notice. Rinse and repeat,  and marvel as she learns to manage her worst excesses so as not to disappoint you.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>You will have to PUSH AWAY a waif to get her to come closer to you. Consoling her,  protecting her,  and drawing her tighter into your orbit will work to do just the opposite of what you intended &#8212; push her into the arms of another <span style="text-decoration:line-through;">sucker</span> man.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>There is really nothing more annoying or frustrating than a waif giving you the silent treatment and allowing other men to flirt with her in front of you. Often,  the frustration is precisely because she does not know what she is doing to you. I&#8217;ve found the best way to deal with these situations is to confront the waif in clear and calm terms and let her know you are aware what is going on. To wit:</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>&#8220;You&#8217;re attitude is telling. If you have something on your mind,  you should let me know,  or go home now. I will only allow women into my life who are capable of getting past their egos and meeting me with an open heart. Improve yourself,  or leave. There are plenty of men who will gladly put up with your shit.&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>If this doesn&#8217;t shake the waif out of her manipulative malaise,  nothing will. And for girls who flirt with other guys in your presence,  you have two options: Fight flirting with flirting,  or confront her,  as I explained above. Showing complete indifference to her provocations will work short term,  but fail long term. You&#8217;re better off sparking her lust for you by flirting with other women in return,  because waifs respond to drama,  their own or yours. Otherwise,  let her betrayal play out,  then later in the evening pull her aside and tell her not to call you again until she&#8217;s ready to respect your boundaries. Odds are you will get a call,  and notice a positive change in her behavior.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>Waifs tend to be drawn to arty,  egocentric men who cope with their women&#8217;s whims by ignoring them (think of Picasso and most of his women).</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>I have dated quite a few Waifs and this is exactly how I dealt with them. Often,  I would confront her drama with my own drama. Dramafest!</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p><em>Tomorrow: The Eternal Ingenue and the Amazonian Alpha!</em></p>
'


gs25 = epub.EpubHtml(title='femme fatales part ii',
file_name='femme_fatales_partii.xhtml',
lang='en')
gs25.content='

 will continue building on <a href="https://heartiste.wordpress.com/2008/09/16/how-to-handle-femmes-fatales/" target="_blank">yesterday&#8217;s post</a> and discuss how to defend yourself against the next femme fatale in Clio&#8217;s list. (As per M. Blowhard&#8217;s suggestion,  I&#8217;ve split up the posts for easier reading.)</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p><strong><a href="http://aliasclio.blogspot.com/2008/07/heartbreakers-7-eternal-ingenue-revised.html" target="_blank">The Eternal Ingenue</a></strong></p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>She can be distinguished from the Waif,  however,  by the fact that where the Waif is often silent,  and usually still,  the Eternal Ingenue is in continual,  graceful,  coltish motion. Nor is she surrounded by an aura of doom-laden unhappiness. She talks a lot. She laughs a good deal. She is above all else,  <em>animated</em>. Prancing,  gambolling,  frolicking like a puppy or a pony,  she is often described as &#8220;charming&#8221; or &#8220;enchanting.&#8221;</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>When guys talk about being attracted to an ethereal &#8220;girlishness&#8221; in women,  they are thinking of ingenues from their pasts. Being a man is tough &#8212; it requires strength,  stoicism,  and seriousness of purpose. We are drawn to the opposite in women,  yang to yin,  and so the ingenue &#8212; the antithesis of the hardened alpha male &#8212; captures our imagination like no other woman can. Of the four femme fatales Clio wrote of,  the Eternal Ingenue comes closest to embodying the essence of the perfect woman. And,  unfortunately,  she is also the most diffcult to tame.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>What makes an ordinary Ingenue into a <em>femme fatale</em>,  one who goes through many men and breaks their hearts,  is that this is a woman &#8220;in love with love, &#8221; who has a dream-image of the perfect love,  and perfect lover,  in her mind,  and is perpetually seeking the one man who can make her feel as she wants to feel.</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Perfection is the enemy of settling. Eternal Ingenues run a risk of growing older alone. They won&#8217;t be cougars &#8212; they&#8217;re too feminine,  cute and coy for that &#8212; but they are the most likely to end up cat ladies babbling to themselves about their potted marigolds. She can avoid this fate by being more hard-headed,  but that has its cost. Cultivation of her pragmatic side will weaken her otherworldy whimsical side,  which is the big generator of her power.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>An element of the Ingenue&#8217;s search for the perfect love is that she must convince herself that all her previous loves were wrong or bad or not &#8220;real&#8221; love at all,  so they didn&#8217;t count,  because,  you see,  for her the only perfect love is first love. As a result of all this self-deception,  she is able to seem virginal even when she is not.</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>This falls right into line with one of my maxims.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p><strong>Maxim #7: The sweeter and more innocent a girl seems,  the greater the likelihood she has been in a gangbang.</strong></p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p><strong>Corollary: Always assume she is a whore. It helps kick the legs out from under the pedestal you will be tempted to put her on,  and it is more often than not true.</strong></p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>You really want to be wary of any woman who overly romaticizes her quest for love. She is probably what Clio described: A woman who will pick you apart for minor faults in the most gratingly passive-aggressive way possible,  and finally leave you on the flimsiest pretext,  often bounding straight into the arms of another man without even a pause for common courtesy.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>This kind of woman is often a natural &#8220;daddy&#8217;s girl, &#8221; though her father may have been rather weak,  but one who either lost her father early,  or has had to share him with other women (her mother,  her sisters,  a step-mother),  and wants him all to herself. She&#8217;ll put her trust in a handful of other women,  but they are often much older than she is. [&#8230;]</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Having dated a number of Eternal Ingenues myself,  I can say this rings true. They either came from divorced families with fathers who bought their love and loyalty,  or they had a caring beta father heading an all-female family who had to divide his love between women. You&#8217;ll know if you are dating a potential Ingenue if you meet her girlfriends and they are all overprotective and annoyingly sassy cougars-in-training. The Eternal Ingenue HATES competition from attractive girls her own age.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>The Ingenue doesn&#8217;t necessarily refuse to be responsible or adult. She simply maintains an air of girlish sweetness and innocence through middle and old age. [&#8230;]</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Unlike Waifs,  Eternal Ingenues can take care of themselves. Which makes them more difficult prey.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <blockquote><p>&#8230;the waif&#8217;s childlike qualities may make a man feel protective: they do not make him feel fatherly. The whole point of the Ingenue is that she brings out this feeling in men. She makes them want to initiate her into the world,  but gently,  in a fatherly way,  with books and talk and advice.</p></blockquote>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Maybe one of the reasons I date so many Eternal Ingenues is that I date <a href="https://heartiste.wordpress.com/2008/02/07/top-two-rules-for-dating-younger-women/" target="_blank">so many younger women</a>. The two go hand in hand. But I&#8217;m not fatherly in the least. Books and talk and advice are beta. The only thing I initiate them into is a world of sexual depravity and soul-rending love addiction.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Men: The Eternal Ingenue is extremely alluring as a sexual conquest. You may bed her,  but winning her over is an entirely separate challenge. Because you are constantly being compared in her mind to her imaginary &#8220;perfect first love&#8221; you will be shit tested until the cougars come home. Because there will be so much competition from other men for her attentions,  you will be subjected to an endless stream of capricious disloyalty from her,  if not outright cheating. It doesn&#8217;t matter how long you&#8217;ve been dating her &#8212; she will be the one keeping you up at night wondering if she&#8217;s tonguing down some random dude on the steps of the National Cathedral at 3 AM,  and the odds are she will be. And,  as a charming but inveterate liar,  she will be the best at hiding her whorish soul from you.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>If you want to break her will,  you must,  first and foremost,  never get thrown back on your heels. If she puts you on the defensive,  consider yourself done. This means being acutely aware of her shit tests,  and passing them with flying colors. Hone your cocky funny skills to perfection,  and parry EVERYTHING she throws your way with the amused mastery of a Jedi player. Example:</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Her: &#8220;Oh GOD,  your taste in music is SO lame. You never play anything I like.&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>You: &#8220;I didn&#8217;t know you were the music czar. I think I&#8217;ll just call you ITunes from now on. Hey,  ITunes,  make me a sandwich!&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Next,  be vigilant about your encroaching neediness. Oh Satan below,  do Ingenues despise needy men. It will take a lot of willpower,  but you should occasionally cancel dates on her and,  when sex is imminent,  find some excuse to walk away,  leaving her horny and unsatisfied. Ingenues love the father figure (are fathers needy? no),  so play up those strengths &#8212; be her authority,  lead,  slap her when necessary,  playfully dismiss her juvenile provocations,  and always be prepared to lay down the law. This last will often mean walking away from her never looking back.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Don&#8217;t feel guilty about dating around on an Ingenue. Her loyalty is razor thin,  so your virtue will gain you nothing. In fact,  an Ingenue will love you more if she suspects you are still playing the field. She needs the challenge,  like she relished the challenge of winning her father&#8217;s affections away from her sister.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Like the Waif,  the Ingenue eight balls her emotional highs from the act of chasing men. She does not suffer long men who chase her &#8212; this fleeting wisp of a woman. Of all the femme fatales,  she yearns to seek your approval the most and wants to actually win it the least. Unlike the Amazonian Alpha,  whom I will discuss tomorrow,  the Ingenue can&#8217;t tolerate heavy-handed qualifying early on,  but she needs to be qualified on a continual basis with a subtler touch. You always have to judge her,  without being judgmental. This is a fine art.</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Her: &#8220;I bought this new dress today. What do you think?&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>You: &#8220;Nice. But I&#8217;m surprised you&#8217;re going in that direction. It seems&#8230; unique.&#8221;</p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   <p>Finally,  the most important advice: Because Eternal Ingenues are &#8220;in love with love&#8221; you should withhold announcing your love for her as long as humanly possible. An old Russian saying: <em>Once a woman captures your heart she loses interest.</em> This is doubly true for the Ingenue. What she doesn&#8217;t know,  or doesn&#8217;t want to know,  is that there never was a perfect love in her life,  and there never will be,  at least not by the impossible standards to which she has elevated the concept. If you lavish her with your love she will find it easier to evaluate her fantasy of love against what you are giving her. You will invariably come up short. So keep her guessing,  keep her in the dark,  and slowly over time she&#8217;ll fill in the blanks and begin imagining that YOUR love is the love she&#8217;s been waiting for.</p>
'


gs26 = epub.EpubHtml(title='femme fatales part iii',
file_name='femme_fatales_partiii.xhtml',
lang='en')
gs26.content='
<h2>Femme Fatales PART III</h2>
<p>In my final installment I will discuss methods for dealing with Clio&#8217;s last,  and scariest,  femme fatale.</p>
<p><strong><a href="http://aliasclio.blogspot.com/2008/07/heartbreakers-8-amazonian-alpha.html" target="_blank">The Amazonian Alpha (AKA Lawyer Chick)</a></strong></p>
<blockquote><p>This woman,  along with the Eternal Ingenue,  is the most likely of all <em>femme fatale</em> types to be perceived as an Iconic Woman. But whereas the Eternal Ingenue inspires dreams of perpetual love and happiness,  the Amazonian Alpha inspires,  in those who fall in love with her,  dreams of glory,  of being raised above all the ordinary people who mill around on the face of the earth. She is the Maverick Alpha&#8217;s natural mate [Editor&#8217;s note: think John and Cindy McCain],  although she may choose a more ordinary Classic Alpha. Often she is unable to find a man she considers worthy of her,  and may remain single.</p></blockquote>
<p>Yes,  Amazonian Alphas who don&#8217;t get married before it&#8217;s too late are the most likely to wind up frightening middle-aged women alone in mansions on hilltops with their pet german shepherds and classical music. The less prideful ones will become cougars &#8212; very VERY aggressive cougars who will stroke your chest on the slimmest pretense.</p>
<blockquote><p>The Amazonian Alpha is usually very intelligent and generally beautiful or at least physically impressive,  being statuesque of build,  like Maud Gonne,  the Irish nationalist who made Yeats miserable,  and often athletic as well. [&#8230;]</p></blockquote>
                                                                                                                                                                                                                                                       <p>My experience with Amazonian Alphas I have dated is that many of them have striking facial bone structure and an often exotic beauty. They are never &#8220;cute&#8221; or pretty in the dull,  washed-out,  southern sorority sister way. They have the kind of angular looks and prominent features that a sizeable minority of men will not find attractive. They are usually taller than average and wear heels everywhere and know how to walk in them. You will never see an Amazonian wear flip-flops. She&#8217;d sooner submit to a beta male like yourself.</p>
                                                                                                                                                                                                                                                       <blockquote><p>In social life,  she can be often recognised as the lone woman talking with a large group of men,  men who laugh at her jokes and who may anxiously ask her opinion about public affairs and actually listen to what she says about them. Random men sledom try to ogle or touch her,  because however beautiful she may be she has a steely eye or haughty deportment that does not bode well for men who behave disrespectfully to her. Her great virtue is strength of character: she will not readily back down and is usually possessed of physical and moral courage. Her great weakness is pride,  which may lead her to serious errors in judgment.</p></blockquote>
                                                                                                                                                                                                                                                       <p>Because Amazonians are the product of the union of a successful alpha male and his beautiful wife,  they often inherit their fathers&#8217; blazing intelligence,  cocksure attitude,  and ambition. If they are lucky,  they will inherit their mothers&#8217; beauty,  but this doesn&#8217;t always happen. More than a few alpha females look like drag queens in pantsuits.</p>
                                                                                                                                                                                                                                                       <p>Men are scared to tangle with the Amazonian because it feels like locking horns with a gung-ho man. They may be nice to look at,  but their afeminine ballbusting personalities can be a total turn-off. Stubborn as mules,  bloated egos that need constant stroking,  and a keen sixth sense for smoking out suitors of bad character,  the Amazonian inspires men to treat her like another man as often as a woman to be seduced. If she&#8217;s smart,  she learns to temper her masculine essence to entrap men of high quality,  because studies are showing that very masculine men with high testosterone are <a href="http://news.bbc.co.uk/2/hi/uk_news/scotland/north_east/7616354.stm" target="_blank">more attracted to very feminine women</a>.</p>
                                                                                                                                                                                                                                                       <blockquote><p>The Alpha Amazon will almost certainly be a Daddy&#8217;s Girl,  but unlike the Neurotic Heartbreaker,  her relationship with her father will not have been interrupted by early death or marital breakdown. Unlike the Eternal Ingenue,  her father is probably also a very successful man,  a dominant Alpha male who was either born to money and power or who acquired it through his own drive or gifts.</p></blockquote>
                                                                                                                                                                                                                                                       <p>Spot on. I remember this one <span style="text-decoration:line-through;">cunt</span> lawyer chick I dated who rhapsodized about her father on our first date:</p>
                                                                                                                                                                                                                                                       <p>&#8220;He&#8217;s a professor at the University of Chicago,  and he&#8217;s a classical pianist. He&#8217;s played in symphonies. He&#8217;s got patents on some of his inventions.&#8221;</p>
                                                                                                                                                                                                                                                       <p>I believe she used the word &#8220;redoubtable&#8221; in her high praise of him. My penis tucked itself in my ass crack.</p>
                                                                                                                                                                                                                                                       <p>Which reminds me&#8230; I haven&#8217;t torn a new one in <a href="https://heartiste.wordpress.com/2007/11/02/i-cant-make-this-shit-up/" target="_blank">lawyer chicks in a while</a>. Where&#8217;s my thesaurus?</p>
                                                                                                                                                                                                                                                       <blockquote><p>The Amazonian Alpha,  although she may break many hearts,  is perhaps alone among all the Heartbreaker types catalogued here in that she very rarely does so deliberately,  nor out of subconscious neurotic compulsion. Her great problem,  and the reason she finds herself breaking hearts,  is the one summarized in Sheryl Crow&#8217;s lament,  &#8220;Are you strong enough to be my man?&#8221;</p></blockquote>
                                                                                                                                                                                                                                                       <p>You will endure the WORST shit tests from the Amazonian Alpha. Lesser men will retreat into belligerence or submissive shoe-gazing. Budding alphas just starting out in the game will overcompensate and allow the brinksmanship to carry on too long,  thinking that sparring with her is the best way to get her in bed. David Alexander will get turned on and swap railfanning stories with her.</p>
                                                                                                                                                                                                                                                       <blockquote><p>She will not respect a man who is not strong enough for her,  and will spend at least part of her life surrounded by male admirers who are not quite equal to her in ability or dominance,  who fight a bit desperately for her notice. Diana Mitford had this problem: she married a sweet-natured,  rather passive man,  mainly to escape from her parents&#8217; control,  and soon after humiliated him by choosing the Maverick Alpha male Oswald Mosley as a lover and publicly flaunting their relationship. Once she married Mosley,  <strong>she accepted his dominance and his infidelities.</strong></p></blockquote>
                                                                                                                                                                                                                                                       <p>This is the interesting thing about women (yes,  all women). If her man is strong enough and gets her thoroughly wet,  she&#8217;ll forgive his sins despite her moral posturing. But woe be the beta who can&#8217;t get her wet; even his minor sins will forever be wielded like a cudgel,  beating him mercilessly into submission,  extracting the last ounce of tribute from his shattered psyche,  and used as flimsy pretext to commit ten times worse sins against him. Which brings us to&#8230;</p>
                                                                                                                                                                                                                                                       <p><strong>Maxim #10: It&#8217;s pussy wetness uber alles.</strong></p>
                                                                                                                                                                                                                                                       <p>A woman&#8217;s shifting,  squirrelly morality and conditional umbrage is also proof of another fact of evolutionary psychology &#8212; men&#8217;s infidelity is not nearly as harmful or unacceptable as women&#8217;s infidelity. I&#8217;ll leave it as an exercise for the reader to figure out why this is so.</p>
                                                                                                                                                                                                                                                       <blockquote><p>Alpha Amazons tend to have more male than female friends,  and to be more at ease in the company of men,  partly because unlike so many women they don&#8217;t mind arguing or fighting for their point of view,  behaviour that makes many women uneasy.</p></blockquote>
                                                                                                                                                                                                                                                       <p>If an Amazonian Alpha has female friends,  she will be THE MOST CHALLENGING cockblock you will ever have the displeasure to encounter. I hope you sacked up before opening her group.</p>
                                                                                                                                                                                                                                                       <blockquote><p>If you find yourself competing with a woman&#8217;s father; if you find that you are always wondering if you are good enough for her,  then it is possible that you have found an Alpha Amazon.</p></blockquote>
                                                                                                                                                                                                                                                       <p>Trenchant.</p>
                                                                                                                                                                                                                                                       <p><strong>Maxim #45: Daddy&#8217;s girls are status whores. You will never measure up to her father. Don&#8217;t even try.</strong></p>
                                                                                                                                                                                                                                                       <p><strong>Corollary: Not trying will turn her on. Be indifferent to her father&#8217;s accomplishments.</strong></p>
                                                                                                                                                                                                                                                       <p>I told the lawyer chick from the above conversation that her father&#8217;s life sounded &#8220;full&#8221;,  and then I quickly changed the subject. I banged her that evening.</p>
                                                                                                                                                                                                                                                       <p>If you are a masochist who likes women with vestigial penises,  then by all means knock yourself out with the Amazonian Alpha. This is what you need to keep in mind to seduce her:</p>
                                                                                                                                                                                                                                                       <ul>
                                                                                                                                                                                                                                                       <li>DON&#8217;T accept her challenges. Parry and dance blithely around her provocations. Thwart her programming. The frame of mind you want to adopt: She is inferior to you. No bitch gets uppity with you.</li>
                                                                                                                                                                                                                                                       <li>DON&#8217;T answer shit test with shit test ad infinitum. She can do that all night,  and you can&#8217;t. Pass the first few shit tests she throws out (and Amazonians front load their shit tests,  unlike Ingenues and Neurotics who shit test forever and ever) and then tell her &#8220;Look,  you don&#8217;t have to be this way. Ssshhh. It&#8217;s time for us to talk like human beings now.&#8221; The goal is to arouse her pussy,  not her pride,  and not her intellect.</li>
                                                                                                                                                                                                                                                       <li>DON&#8217;T brag about your achievements,  especially in response to her own gleefully recounted resume. She will see any bragging as compensation. It&#8217;s actually better for you to make light of your station in life. &#8220;Yeah,  I just bought a new scooter. You&#8217;ll be the belle of the ball showing up riding in the flower basket I put over the handlebars!&#8221;.</li>
                                                                                                                                                                                                                                                       <li>DON&#8217;T be ordinary. You can coast with drinks at a trendy lounge with an artsy chick,  but you&#8217;ll want to step it up for an Amazonian. Take her on an adventure. Samba dancing at midnight,  bingo at a gay club,  berry picking in the countryside&#8230; you get the idea.</li>
                                                                                                                                                                                                                                                       <li>DON&#8217;T be beta. This is true for any woman,  but never moreso than with the Alpha chick. You&#8217;ve gotta show real dominance,  and that means never asking questions,  being decisive,  leading her on the dance floor,  and choosing her drinks for her. She will try to push you around,  probing for weak spots in your underbelly,  and you have to stay solid,  armored,  like a concrete bunker.</li>
                                                                                                                                                                                                                                                       <li>DON&#8217;T talk about her father.</li>
                                                                                                                                                                                                                                                       <li>DO stroke her ego. This is really the only type of girl you can genuinely compliment on the first date without seeming beta. Keep your compliments focused on her smarts and her life-affirming gusto. She&#8217;ll eat it up.</li>
                                                                                                                                                                                                                                                       <li>DO qualify her hard. You won&#8217;t run the risk of overqualifying yourself with this girl like you would with the other types of femmes fatales. Remember,  she already thinks she is above you,  so constantly screening her for compatibility will only push her closer to your level,  never below it. Example: &#8220;So you can cook,  but you don&#8217;t know how to cook Thai-Mongolian fusion? I would&#8217;ve thought of all the girls I&#8217;ve met you would be the one who could.&#8221;</li>
                                                                                                                                                                                                                                                       <li>DO fuck her like a silverback gorilla. Hair pulling is just the start. Practice your wind-up; you&#8217;re going to be smacking her ass so hard your dick will feel the sting in her pussy.</li>
                                                                                                                                                                                                                                                       <li>DO dump her after getting your rocks off. Why would you want to spend your life with a nutcrushing battleaxe like this?</li>
                                                                                                                                                                                                                                                       </ul>
                                                                                                                                                                                                                                                       <p>Dating ballbusters has really hardened me. I&#8217;m a better man for it.</p>
'


gs27 = epub.EpubHtml(title='BB',
file_name='BB.xhtml',
lang='en')
gs27.content='
<h2>Should You Call Out A Girl&#8217;s Bad&nbsp;Behavior?</h2>

'


























tion of whether to call out,  or confront,  a girl over any behavior of hers that is disrespectful to you is less cut-and-dried than it sounds. For instance,  what do you do when you ask a girl out through text and she replies a day later? The he-man,  tough guy traditionalists would say you don&#8217;t put up with shit from women,  you be a man,  and that means reprimanding women when they get out of line. Ok,  great,  but will that get you any closer to getting laid,  which,  remember,  is your primary goal?</p>
<p>(He-men will say to that &#8220;Getting laid is less important than sticking up for your principles.&#8221; I&#8217;d tell them that having principles is fine up until the point those principles become recurring obstacles getting in the way of enjoying a satisfying love life. After which point it&#8217;s time to reevaluate your principles so that they&#8217;re geared to your personal advantage.)</p>
    <p>Back to the scenario of the girl who texts a day late. It just so happens that I put the &#8220;calling out&#8221; theory to the test about four years ago when I went through a string of dates and flings with about fifteen girls in two months. Three of the girls totally flaked on me: two cancelled a first date at the last minute and one stood me up. A fourth girl took forever to reply to my texts. I was pissed at these flakes and was searching for a fail-safe method to deal with them and bolster my dignity in the process. At that time,  I had been hearing a lot from a couple of naturals I knew who claimed that they never hesitated to call girls out on their shitty behavior. They recommended I do the same. Up till then,  I was fairly content to just ignore or tease girls when they acted out their <a href="https://heartiste.wordpress.com/2007/05/22/flake-odds-point-system/" target="_blank">female flake algorithm</a>.</p>
    <p>To the two girls who cancelled at the last minute,  I texted one and left a voicemail with the other expressing my displeasure along the lines of (paraphrasing) &#8220;My time is valuable. Last minute blow-offs are not cool.&#8221; To the girl who stood me up,  I left an angrier text telling her not to make plans if she wasn&#8217;t going to see them through. The fourth girl who waited forever to reply to my texts got this in response: &#8220;I don&#8217;t hang with girls who can&#8217;t be bothered to text back in a reasonable time frame.&#8221;</p>
    <p>The idea here was to rattle the girls with a strong,  but non-needy,  alpha display that they normally didn&#8217;t experience from most men they flaked on. In theory,  it sounded plausible. However,  in practice it was a total failure. None of the girls ever replied to my stern rebukes.</p>
    <p>Conclusion: disciplining prospects = failed game.</p>
    <p>Early in the seduction process,  before you have cemented the bond with a few nights of fuckfare,  stern paternal rebukes,  however much delivered from a position of non-neediness,  will turn girls off. A girl will never &#8212; I mean NEVER &#8212; accept that she bears responsiblity for her poor behavior. I don&#8217;t care if her fucking life is on the line,  she&#8217;ll find a way to excuse her actions. Calling an inconsiderate girl out will only add pellets to her hamster&#8217;s food dish,  and she&#8217;ll happily rationalize your scolding so that her decision to flake seems like a good one to her: &#8220;Wow,  that guy is weird. Good thing we didn&#8217;t meet up.&#8221;</p>
    <p>If you want to blow up any bridges to sex for the thrill of chastising a girl when she&#8217;s acting like a bitch,  and for helping other guys out who might have to deal with her in the future,  I say go for it. I suggest brutally dressing a girl down in front of a group of her friends,  or in a public place. &#8220;Did your parents raise you to be this way?&#8221; is a good line that&#8217;ll shut most shrikes up.</p>
    <p>But I wouldn&#8217;t make a habit of it. The best way to handle misbehaving,  flaky girls that most consistently results in furthering positive interactions with the girls (should you choose to further them) is to do the following,  in no specific order of effectiveness:</p>
    <p>&#8211; Ignore<br />
    &#8211; Tease<br />
    &#8211; Misdirect<br />
    &#8211; Demote</p>
    <p>Here are some examples of the above methods.</p>
    <p>Ignore:<br />
    Self-explanatory. A girl texts you a day later,  you don&#8217;t immediately reply,  and you don&#8217;t let her know that her tardiness even registered in your consciousness. You act like this is just how girls are,  and they deserve no better in return. Proceed as if nothing is wrong.</p>
    <p>Tease:<br />
    &#8220;-10 points for lack of prompt reply. you&#8217;re losing me. you got ground to make up.&#8221; Also see <a href="https://heartiste.wordpress.com/2009/02/02/reversing-a-flake/" target="_blank">this post</a> for more examples of teasing a girl to reverse her flaking.</p>
    <p>Misdirect:<br />
    &#8220;What was this about?&#8221; Forces girl to explain the context of her reply,  which reframes back in your favor. Another good misdirection involves answering as if you were talking to a different girl,  which will compel her to figure out what you mean: &#8220;Ok,  i&#8217;ll drop my stuff off at your place later&#8221;,  to which she will likely ask &#8220;what?&#8221; and then you reply &#8220;my mistake. what&#8217;s up?&#8221; (credit: Lara).</p>
    <p>Demote:<br />
    (credit: YaReally) I wouldn’t call her out I’d just act as if I have 10 playboy models on the go and simply reply “sorry too slow lol made other plans. Next time” and then not respond for a few days. That teaches the lesson of “don’t dick around” without coming off insecure and angry.</p>
    <p>I can say with a good degree of assurance that calling girls out for crappy behavior is counter-productive in the early stages of a seduction or dating trajectory. It might make you feel better,  but it won&#8217;t pry open many vaginas. It&#8217;s a different story once you&#8217;ve been sexing a girl or are in a relationship; at that stage of the fuck cycle,  you should establish your dominance when she starts pulling shit on you to test your alpha mettle. Bemused mastery is the alpha attitude women love,  and there isn&#8217;t much room for indignant anger in that attitude. Especially at the beginning,  when neither of you knows each other very well.</p>
    <p>If you act like the typical shit that girls pull gets to you,  then she&#8217;ll think (rightly) that you don&#8217;t have much experience with women.</p>qqquBook Spine

book.add_item(intro)
book.add_item(foundations)
book.add_item(f1)
book.add_item(f2)
book .add_item(f3)
book .add_item(f5)
book.add_item(f6)
book.add_item(f7)
book.add_item(f8)
book.add_item(f9)
book.add_item(f10)
book.add_item(f11)
book.add_item(f12)
book.add_item(f13)
book.spine = ['cover ', intro, foundations, f1, f2, f3, f4, f5 , f6, f7, f8,
f9, f10, f11, f12 , f13]

# create epub file
epub.write_epub('roissy.epub', book, {})
