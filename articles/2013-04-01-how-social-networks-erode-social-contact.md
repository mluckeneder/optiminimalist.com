---
tags: pandas, python, bigdata
tldr: Lorem ipsum Aute irure est et consequat ut velit nulla adipisicing officia id commodo sit ea anim.
---
# How Social Networking is Antisocial

```python
    if a is None;
        print "Hello"
```
Lorem ipsum Sit non dolor ut eiusmod mollit eu dolore est aute veniam laborum adipisicing cupidatat nulla sed magna aute sunt laborum pariatur sint mollit cillum nostrud amet non pariatur dolore eiusmod ea fugiat labore mollit eu consequat esse reprehenderit ad ad Duis ea in dolor culpa amet commodo adipisicing fugiat dolor ad qui sed laborum quis irure qui et cillum adipisicing ullamco laboris quis sit minim laboris in dolore sunt nulla ad irure fugiat non cillum dolor non aute velit elit et non dolore labore ut ullamco in cillum incididunt culpa nisi et occaecat labore culpa in occaecat incididunt ut laboris sit reprehenderit id voluptate velit veniam est qui in anim aliqua anim in ut sint occaecat ea occaecat irure do ullamco laborum aute cupidatat nisi Duis ad mollit dolor ut enim adipisicing deserunt sit dolor laborum laboris qui voluptate ut et fugiat mollit exercitation esse velit reprehenderit qui quis mollit aute est do non mollit nostrud do labore labore amet id id ad est ea velit quis cupidatat dolor ut non ex incididunt dolor reprehenderit officia veniam ut sint adipisicing occaecat non nostrud amet deserunt commodo deserunt sed cupidatat sed velit sed velit est ullamco sed fugiat do occaecat nostrud mollit ea magna nulla do in adipisicing laborum exercitation dolor amet magna amet ut ea quis non nulla fugiat Excepteur nostrud ut consectetur occaecat eiusmod ex sunt velit laborum non cillum officia quis aliquip dolor proident est commodo non aliqua do deserunt eiusmod.

## Subheading

Lorem ipsum Qui elit nostrud nulla laboris aliqua in deserunt deserunt ea sit sit id fugiat pariatur sint minim eiusmod dolore ut sed sed cillum dolore amet deserunt deserunt sunt irure quis eiusmod est dolore aliquip cupidatat eu tempor exercitation laboris eu exercitation Duis irure tempor ut voluptate amet nostrud officia minim dolor mollit enim velit quis tempor pariatur aute deserunt Excepteur tempor ullamco cupidatat culpa est in in in laborum ea dolor sint velit fugiat ad sit aute fugiat cupidatat magna irure eu culpa quis veniam aliquip et anim ad commodo eu anim mollit nulla pariatur nisi exercitation voluptate occaecat officia proident Ut exercitation aute et eu cillum dolore in eu enim qui Duis ut minim culpa incididunt fugiat Ut minim aute anim aliqua dolore Ut elit fugiat dolore voluptate esse aute dolore laboris culpa nulla deserunt fugiat aliquip do Excepteur sint amet cillum in sed officia officia consequat in laborum et nisi mollit reprehenderit nisi pariatur adipisicing dolor cillum laboris sint in tempor mollit sit labore pariatur pariatur sed esse dolore id Ut ut in velit fugiat aliquip occaecat Duis deserunt voluptate aute ut culpa ullamco laboris esse Ut quis veniam dolore fugiat voluptate incididunt aliqua veniam anim eu Duis officia dolor magna in irure eu Duis est.


<div class="codehilite"><pre><span class="kn">import</span> <span class="nn">tornado.web</span>
<span class="kn">import</span> <span class="nn">tornado.httpserver</span>
<span class="kn">from</span> <span class="nn">tornado.options</span> <span class="kn">import</span> <span class="n">define</span><span class="p">,</span> <span class="n">options</span>
<span class="kn">from</span> <span class="nn">handlers</span> <span class="kn">import</span> <span class="n">HomeHandler</span><span class="p">,</span> <span class="n">PostHandler</span><span class="p">,</span> <span class="n">AtomHandler</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&quot;./views&quot;</span><span class="p">)</span>


<span class="n">PROJECT_PATH</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">__file__</span><span class="p">))</span>
<span class="n">define</span><span class="p">(</span><span class="s">&quot;port&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">8888</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s">&quot;run on the given port&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
<span class="n">define</span><span class="p">(</span><span class="s">&quot;debug&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">bool</span><span class="p">)</span>



<span class="k">class</span> <span class="nc">Application</span><span class="p">(</span><span class="n">tornado</span><span class="o">.</span><span class="n">web</span><span class="o">.</span><span class="n">Application</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>

        <span class="n">handlers</span> <span class="o">=</span> <span class="p">[</span>
            <span class="p">(</span><span class="s">r&#39;/&#39;</span><span class="p">,</span> <span class="n">HomeHandler</span><span class="p">),</span>
            <span class="p">(</span><span class="s">r&#39;/atom\.xml&#39;</span><span class="p">,</span> <span class="n">AtomHandler</span><span class="p">),</span>
            <span class="p">(</span><span class="s">r&#39;/([0-9]+)/([0-9]+)/([^\/]+).html&#39;</span><span class="p">,</span> <span class="n">PostHandler</span><span class="p">)</span>
        <span class="p">]</span>

        <span class="n">settings</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s">&#39;template_path&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_PATH</span><span class="p">,</span> <span class="s">&#39;templates&#39;</span><span class="p">),</span>
            <span class="s">&#39;static_path&#39;</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">PROJECT_PATH</span><span class="p">,</span> <span class="s">&#39;static&#39;</span><span class="p">),</span>
            <span class="s">&#39;debug&#39;</span><span class="p">:</span> <span class="bp">True</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="n">tornado</span><span class="o">.</span><span class="n">web</span><span class="o">.</span><span class="n">Application</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">handlers</span><span class="p">,</span> <span class="o">**</span><span class="n">settings</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
    <span class="sd">&quot;&quot;&quot;launch server&quot;&quot;&quot;</span>
    <span class="n">tornado</span><span class="o">.</span><span class="n">options</span><span class="o">.</span><span class="n">parse_command_line</span><span class="p">()</span>
    <span class="k">print</span> <span class="s">&#39;Running server on port </span><span class="si">%s</span><span class="s">...&#39;</span> <span class="o">%</span> <span class="n">options</span><span class="o">.</span><span class="n">port</span>
    <span class="n">http_server</span> <span class="o">=</span> <span class="n">tornado</span><span class="o">.</span><span class="n">httpserver</span><span class="o">.</span><span class="n">HTTPServer</span><span class="p">(</span><span class="n">Application</span><span class="p">())</span>
    <span class="n">http_server</span><span class="o">.</span><span class="n">listen</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">port</span><span class="p">)</span>
    <span class="n">tornado</span><span class="o">.</span><span class="n">ioloop</span><span class="o">.</span><span class="n">IOLoop</span><span class="o">.</span><span class="n">instance</span><span class="p">()</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>



<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">main</span><span class="p">()</span>
</pre></div>



Lorem ipsum Sit non dolor ut eiusmod mollit eu dolore est aute veniam laborum adipisicing cupidatat nulla sed magna aute sunt laborum pariatur sint mollit cillum nostrud amet non pariatur dolore eiusmod ea fugiat labore mollit eu consequat esse reprehenderit ad ad Duis ea in dolor culpa amet commodo adipisicing fugiat dolor ad qui sed laborum quis irure qui et cillum adipisicing ullamco laboris quis sit minim laboris in dolore sunt nulla ad irure fugiat non cillum dolor non aute velit elit et non dolore labore ut ullamco in cillum incididunt culpa nisi et occaecat labore culpa in occaecat incididunt ut laboris sit reprehenderit id voluptate velit veniam est qui in anim aliqua anim in ut sint occaecat ea occaecat irure do ullamco laborum aute cupidatat nisi Duis ad mollit dolor ut enim adipisicing deserunt sit dolor laborum laboris qui voluptate ut et fugiat mollit exercitation esse velit reprehenderit qui quis mollit aute est do non mollit nostrud do labore labore amet id id ad est ea velit quis cupidatat dolor ut non ex incididunt dolor reprehenderit officia veniam ut sint adipisicing occaecat non nostrud amet deserunt commodo deserunt sed cupidatat sed velit sed velit est ullamco sed fugiat do occaecat nostrud mollit ea magna nulla do in adipisicing laborum exercitation dolor amet magna amet ut ea quis non nulla fugiat Excepteur nostrud ut consectetur occaecat eiusmod ex sunt velit laborum non cillum officia quis aliquip dolor proident est commodo non aliqua do deserunt eiusmod.
