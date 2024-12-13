# Table of Contents

- **Section 1**: [Software Architecture Mindmap](#software-architecture-mindmap)
- **Section 2**: [Software Architecture Reference](#software-architecture-reference)
  - [Cloud Architecture](#cloud-architecture)
  - [Computer Science courses](#computer-science-courses)
  - [Industry Trends](#industry-trends)
  - [Newsletter](#newsletter)
  - [Tools](#tools--research)
  - [Engineering blog](#engineering-blog)
  - [Computer Science Books](#computer-science-books)
- **Section 3**: [Computer Science Papers](#computer-science-papers)
  - [Computer Science Papers Every Developers Should Read](#computer-science-papers-every-developers-should-read)
  - [Distributed Systems!](#distributed-systems)
  - [25 Papers That Completely Transformed the Computer World](#25-papers-that-completely-transformed-the-computer-world)
- **Section 4**: [Data Science (ML/NN)](#data-science-mlnn)
  - [Free e-books](#free-e-books)
  - [GitHub](#github)
- **Section 5**: [Terminology and Comparisons](#terminology-and-comparisons)

## Software Architecture Mindmap

Software terminologies and concepts, software architecture overview

Summarized the keywords and solutions have faced in my learning and experience.

<img src="./Preview.png" width="50%">

- Full Version

`Software_Architecture_Mindmap.png`

Three main pillars upon software architecture

- Modern Application Development

- Cloud Computing (AWS/Azure/GCP)

- Data Science (ML/NN)

and

Numerous technologies and methodologies.

ⓒ 2022. (https://github.com/kimtth) all rights reserved.

This mindmap created by `https://app.mindmapmaker.org/`

---

## Software Architecture Reference

- [System Design 101](https://github.com/ByteByteGoHq/system-design-101): ByteByteGo
- [Awesome Lists](https://github.com/sindresorhus/awesome): 😎 Awesome lists about all kinds of interesting topics / `awesome.re` / [github topic](https://github.com/topics/awesome)
- [Awesome Software Architecture (simskij)](https://github.com/simskij/awesome-software-architecture)
- [Awesome Software Architecture](https://github.com/mehdihadeli/awesome-software-architecture): A curated list of awesome articles, videos, and other resources to learn and practice software architecture, patterns, and principles
- [Software Architecture Books](https://github.com/mhadidg/software-architecture-books): A comprehensive list of books on Software Architecture
- [System Design](https://github.com/karanpratapsingh/system-design): Learn how to design systems at scale and prepare for system design interviews
- [Microsoft .NET Application Architecture - Reference Apps](https://github.com/dotnet-architecture/eShopOnWeb)
- [Software Architecture Books](https://github.com/mhadidg/software-architecture-books)
- [System Design Fight Club](https://github.com/systemdesignfightclub/SDFC)
- [System Design - Neo Kim](https://github.com/systemdesign42/system-design)
- [Awesome System Design Resources](https://github.com/ashishps1/awesome-system-design-resources)

---

- [InfoQ](https://www.infoq.com): News and Articles
- [Dzone](https://dzone.com/): RefCards and Trend Reports
- [Thoughtworks](https://www.thoughtworks.com/radar): Technology Radar
- [Microsoft Learn](https://learn.microsoft.com/en-us/): Documentation and Code samples
- [Trendshift](https://trendshift.io/): GitHub Trending repositories
- [Design Gurus](https://www.designgurus.io/): Portal For Tech Interviews
- [System Design Blueprint: The Ultimate Guide](https://blog.bytebytego.com/p/ep56-system-design-blueprint-the)

---

- [Google SRE Handbook](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals)

    <details>
    <summary>Expand</summary>

    🔹 `Latency` is the response time of your application, usually expressed in milliseconds

    🔹 `Throughput` is how many transactions per second or minute your application can handle

    🔹 `Errors` is usually measured in a percent of

    🔹 `Saturation` is the ability of your application to use the available CPU and Memory

    </details>
- [InfoQ minibooks](https://www.infoq.com/minibooks/): Architectures You’ve Always Wondered About .. [2021](./files/minibooks/AYAWA-2021-1635782607730.pdf) / [2023](./files/minibooks/AYAWA-2023-1685636455618.pdf) / [2024](./files/minibooks/AYAWA-2024-1712241257109.pdf) / [Cell-Based Architecture](https://www.infoq.com/minibooks/cell-based-architecture-2024)

### Building from scratch

- [Web Browser Engineering](https://browser.engineering/): Building a basic but complete web browser from scratch
- [Curated list of project-based tutorials](https://github.com/practical-tutorials/project-based-learning)
- [Master programming by recreating your favorite technologies from scratch](https://github.com/codecrafters-io/build-your-own-x)
- [Build frontend applications at scale](https://frontendatscale.com/courses/frontend-architecture/)

### Cloud Architecture

- [AWS to Azure services comparison](https://learn.microsoft.com/en-us/azure/architecture/aws-professional/services)
- [Google Cloud to Azure services comparison](https://learn.microsoft.com/en-us/azure/architecture/gcp-professional/services)
- [Compare AWS and Azure services to Google Cloud](https://cloud.google.com/docs/get-started/aws-azure-gcp-service-comparison)
- [Microsoft Azure Developer's Cheat Sheet](https://github.com/milanm/azure-cheat-sheet): Every product, feature and service in the Azure family
- [Azure Cloud Adoption Framework :CAF](https://learn.microsoft.com/en-gb/azure/cloud-adoption-framework/): organization-wide adoption guidance
- [Azure Well-architected Framework :WAF](https://learn.microsoft.com/en-us/azure/well-architected/): workload-focussed design and continuous improvement guidance
- [Azure Architecture Center :AAC](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/?product=popular): architecture patterns and reference architectures
  - [Best practices in cloud applications](https://learn.microsoft.com/en-us/azure/architecture/best-practices/index-best-practices)
  - [Cloud Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/)
  - [Landing zone](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/azure-virtual-desktop/design-guide?tabs=baseline)
  - [Resources for architects and developers of multitenant solutions](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/related-resources)
  - [Data partitioning strategies](https://learn.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning-strategies)
  - [Azure FinOps Guide](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/the-azure-finops-guide/bc-p/4237205#M1023)
  - [Modern Web App pattern for .NET](https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/enterprise-app-patterns/modern-web-app/dotnet/guidance) [git](https://github.com/Azure/modern-web-app-pattern-dotnet)

<details>
    <summary>Expand</summary>

    🔹 Abstractly speaking, a landing zone helps you plan for and design an Azure deployment, by conceptualizing a designated area for placement and integration of resources. 

    There are two types of landing zones:

    1. `platform landing zone`: provides centralized enterprise-scale foundational services for workloads and applications.
    2. `application landing zone`: provides services specific to an application or workload.
</details>

### Computer Science courses

- [Kaggle Solutions and Ideas](https://github.com/faridrashidi/kaggle-solutions): Collection of Kaggle Solutions and Ideas
- [Best-of Machine Learning with Python](https://github.com/ml-tooling/best-of-ml-python): A ranked list of awesome machine learning Python libraries. Updated weekly.
- [freeCodeCamp](https://www.freecodecamp.org): Learn to code for free. [youtube](https://www.youtube.com/freecodecamp)
- [Ultimate Collection of 60 YouTube Courses for 21 Programming Languages](https://dev.to/arjuncodess/ultimate-collection-of-60-youtube-courses-for-21-programming-languages-mega-list-47b5)
- [Computer Science courses with video lectures](https://github.com/Developer-Y/cs-video-courses)

### Industry Trends

- [Software Industry Statistics](https://www.statista.com/markets/418/topic/484/software/#overview): Statista Industry Insight
- [Gartner Top Strategic Technology Trends 2024](https://www.gartner.com/en/articles/gartner-top-10-strategic-technology-trends-for-2024)
- [MAD (ML/AI/Data) Landscape](https://mad.firstmark.com/)
- [Hype Cycle for Emerging Technologies 2024](https://www.gartner.com/en/newsroom/press-releases/2024-08-21-gartner-2024-hype-cycle-for-emerging-technologies-highlights-developer-productivity-total-experience-ai-and-security)
- [Microsoft Digital Defense Report](https://aka.ms/MDDR)

### Newsletter

- [Substack Leaderboard](https://substack.com/browse/technology): Newsletter
- [daily.dev](https://app.daily.dev): Personalized news feed

### Tools & Research

- [Algorithm Visualizer](https://github.com/algorithm-visualizer/algorithm-visualizer): Interactive Online Platform that Visualizes Algorithms from Code
- [Hello Algo](https://www.hello-algo.com/en/)
- [Wikipedia: List of algorithms](https://www.wikiwand.com/en/articles/List_of_algorithms)
- [OOP Design Patterns](https://refactoring.guru/design-patterns)
- [Dev Encyclopedia](https://devpedia.dev/): Encyclopedia for developers / [git](https://github.com/Buzzpy/Dev-Encyclopedia)
- [Data Engineering Wiki](https://dataengineering.wiki/Index)
- [Best Kubernetes Tools](https://bluelight.co/blog/best-kubernetes-tools): Bluelight Consulting
- [PostgreSQL Wiki: Don't Do This](https://wiki.postgresql.org/wiki/Don%27t_Do_This)
- [Power BI DAX Patterns](https://www.daxpatterns.com/patterns/)
- [Semantic Scholar > Semantic Reader](https://www.semanticscholar.org)
- [AI by Hand](https://by-hand.ai)
- Visualizing relationships between research: [Litmaps](https://www.litmaps.com):  / [Connected Papers](https://www.connectedpapers.com/)
- Finding Papers: [Ask R Discovery](https://discovery.researcher.life/ask-rdiscovery) / [scite_](https://scite.ai/)
- Visualizer for neural network: [netron](https://github.com/lutzroeder/netron)
- [Excalidraw](https://excalidraw.com/)
- [eraser.io](https://www.eraser.io/): Diagram as Code

### Engineering blog

- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
- [Azure Architecture Blog](https://techcommunity.microsoft.com/t5/azure-architecture-blog/bg-p/AzureArchitectureBlog)
- [GCP Cloud Blog](https://cloud.google.com/blog)
- [Netflix TechBlog](https://medium.com/netflix-techblog)
- [Uber Blog](http://eng.uber.com/)
- [The Cloudflare Blog](https://blog.cloudflare.com/)
- [Engineering at Meta](https://engineering.fb.com/)
- [LinkedIn Engineering](https://engineering.linkedin.com/blog)
- [Stripe Blog: Engineering](https://stripe.com/blog/engineering)
- [Discord Blog: Engineering & Developers](https://discord.com/category/engineering)
- [Slack Engineering](https://slack.engineering/)
- [79 Engineering Blogs To Level Up Your System Design Skills](https://blog.bytebytego.com/p/79-engineering-blogs-to-level-up)

### Other Topics

- [How to Architect Software for a Greener Future](https://www.infoq.com/articles/architect-software-for-greener-future)
- [Generative Search: Practical Advice for Retrieval Augmented Generation (RAG)](https://www.infoq.com/presentations/vector-embedding-llm/)
- [What are the Greenest Programing Languages?](https://datasciencelearningcenter.substack.com/p/what-are-the-greenest-software-programming)
- [Frugal Architect Handbook](http://thefrugalarchitect.com/)

### Computer Science Books

1. General
    - [The Pragmatic Programmer](https://www.amazon.com/dp/020161622X) by David Thomas and Andrew Hunt
    - [Modern Software Engineering](https://www.amazon.com/dp/0137314914) by David Farley
    - [Code Complete](https://www.amazon.com/dp/0735619670) by Steve McConnell
    - [Software Engineering at Google](https://www.amazon.com/dp/1492082791) by Titus Winters, Tom Manshreck, and Hyrum Wright

2. Good Practices
    - [Clean Code](https://www.amazon.com/dp/0132350882) by Uncle Bob Martin
    - [Head First Design Patterns](https://www.amazon.com/dp/0596007124) by Eric Freeman
    - [Refactoring](https://www.amazon.com/dp/0201485672) by Martin Fowler
    - [Design Patterns](https://www.amazon.com/dp/0201633612) by Eric Gamma and Others

3. Data Structures and Algorithms
    - [Grokking Algorithms](https://www.amazon.com/dp/1617292230) by Aditya Bhargava
    - [Introduction to Algorithms](https://www.amazon.com/dp/0262033844) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein
    - [Cracking the Coding Interview](https://www.amazon.com/dp/0984782850) by Gayle Laakmann McDowell

4. Data
    - [Designing Data-Intensive Applications](https://www.amazon.com/dp/1449373321) by Martin Kleppman
    - [Learning SQL](https://www.amazon.com/dp/0596520832) by Alan Beaulieu

5. Testing
    - [Growing Object-Oriented Software, Guided by Tests](https://www.amazon.com/dp/0321503627) by Steve Freeman
    - [Unit Testing Principles, Practices, and Patterns](https://www.amazon.com/dp/1617296279) by Vladimir Khorikov
    - [The Art of Unit Testing](https://www.amazon.com/dp/1617290890) by Roy Osherove
    - [TDD by Example](https://www.amazon.com/dp/0321146530) by Kent Beck

6. Software Architecture
    - [Fundamentals Of Software Architecture](https://www.amazon.com/dp/1492043451) by Mark Richards and Neil Ford
    - [Clean Architecture](https://www.amazon.com/dp/0134494164) by Uncle Bob Martin
    - [Software Architecture: The Hard Parts](https://www.amazon.com/dp/1492086894) by Neal Ford, Mark Richards, Pramod Sadalage, and Zhamak Dehghani
    - [Domain-Driven Design Quickly](https://www.amazon.com/dp/1411609255) by Abel Avram and Floyd Marinescu
    - [A Philosophy of Software Design](https://www.amazon.com/dp/1732102201) by John Ousterhout
    - [System Design Interview](https://www.amazon.com/dp/1736049119) by Alex Xu
    - [Domain-Driven Design](https://www.amazon.com/dp/0321125215) by Eric Evans

7. Distributed Systems
    - [Understanding Distributed Systems](https://www.amazon.com/dp/1838430210) by Roberto Vitillo
    - [Designing Distributed Systems](https://www.amazon.com/dp/1491983647) by Brendan Burns

8. DevOps
    - [DevOps Handbook](https://www.amazon.com/dp/1942788002) by Gene Kim, Patrick Debois, John Willis, and Jez Humble
    - [Continuous Delivery](https://www.amazon.com/dp/0321601912) by Jez Humble and David Farley
    - [Accelerate](https://www.amazon.com/dp/1942788339) by Nicole Forsgren, Jez Humble, and Gene Kim

9. Machine Learning
    - [The Hundred-Page Machine Learning Book](https://www.amazon.com/dp/199957950X) by Andriy Burkov
    - [Designing Machine Learning Systems](https://www.amazon.com/dp/1098107969) by Chip Huyen

- [ref](https://newsletter.techworld-with-milan.com/p/learn-things-that-dont-change) | [ref](https://blog.bytebytego.com/p/ep111-my-favorite-10-books-for-software) | [ref](https://github.com/mhadidg/software-architecture-books)

## Computer Science Papers

### Computer Science Papers Every Developers Should Read

- [ref](https://x.com/milan_milanovic/status/1747167493553062398?s=20)

1. [On the Criteria To Be Used in Decomposing Systems into Modules (1972)](https://win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf): D.L. Parnas  
2. [An Axiomatic Basis for Computer Programming (1969)](http://sunnyday.mit.edu/16.355/Hoare-CACM-69.pdf): C.A.R. Hoare  
3. [Time, Clocks, and the Ordering of Events in a Distributed System (1978)](https://microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/): L. Lamport  
4. [Out of the Tar Pit (2006)](https://curtclifton.net/papers/MoseleyMarks06a.pdf): B. Moseley, P. Marks  
5. [Dynamo: Amazon’s Highly Available Key-value Store (2007)](https://allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf): G. DeCandia et al.  
6. [MapReduce: Simplified Data Processing on Large Clusters (2004)](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf): J. Dean, S. Ghemawat  
7. [A Note On Distributed Computing (1994)](https://scholar.harvard.edu/files/waldo/files/waldo-94.pdf): J. Waldo, G. Wyant, A. Wollrath, S. Kendall  
8. [A Metrics Suite for Object-Oriented Design (1994)](https://sites.pitt.edu/~ckemerer/CK%20research%20papers/MetricForOOD_ChidamberKemerer94.pdf): S.R. Chidamber  
9. [A Relational Model of Data for Large Shared Data Banks (1969)](https://dl.acm.org/doi/10.1145/362384.362685): E.F. Codd  
10. [Why Functional Programming Matters (1990)](https://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf): J. Hughes  

### Distributed Systems!

- Here's a reading list of 70+ Distributed Systems papers *mostly from conferences in just last 2 years*! [70+ Distributed Systems papers](https://docs.google.com/document/d/1XX5ksgLVnkPE-dfeVDZPlv5NMbgxJqWmi13YEQt1t1o/edit) [Jan 2024]

### 25 Papers That Completely Transformed the Computer World

- [ref](https://blog.bytebytego.com/p/ep111-my-favorite-10-books-for-software) [May 2024]

1. [Dynamo](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf): Amazon’s Highly Available Key Value Store  
2. [Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf): Insights into a highly scalable file system  
3. [Scaling Memcached at Facebook](https://research.facebook.com/file/839620310074473/scaling-memcache-at-facebook.pdf): A look at the complexities of caching  
4. [BigTable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf): The design principles behind a distributed storage system  
5. [Borg](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf): Large Scale Cluster Management at Google  
6. [Cassandra](https://www.cs.cornell.edu/projects/ladis2009/papers/lakshman-ladis2009.pdf): A look at the design and architecture of a distributed NoSQL database  
7. [Attention Is All You Need](https://arxiv.org/abs/1706.03762): Into a new deep learning architecture known as the transformer  
8. [Kafka](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/Kafka.pdf): Internals of the distributed messaging platform  
9. [FoundationDB](https://www.foundationdb.org/files/fdb-paper.pdf): A look at how a distributed database works  
10. [Amazon Aurora](https://web.stanford.edu/class/cs245/readings/aurora.pdf): How Amazon provides high availability and performance  
11. [Spanner](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf): Design and architecture of Google’s globally distributed database  
12. [MapReduce](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/16cb30b4b92fd4989b8619a61752a2387c6dd474.pdf): A detailed look at how MapReduce enables parallel processing of massive volumes of data  
13. [Shard Manager](https://dl.acm.org/doi/pdf/10.1145/3477132.3483546): Understanding the generic shard management framework  
14. [Dapper](https://static.googleusercontent.com/media/research.google.com/en//archive/papers/dapper-2010-1.pdf): Insights into Google’s distributed systems tracing infrastructure  
15. [Flink](https://www.researchgate.net/publication/308993790_Apache_Flink_Stream_and_Batch_Processing_in_a_Single_Engine): A detailed look at the unified architecture of stream and batch processing  
16. [A Comprehensive Survey on Vector Databases](https://arxiv.org/pdf/2310.11703.pdf)  
17. [Zanzibar](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/d84ab6c93881af998de877d0070a706de7bec6d8.pdf): A look at the design, implementation, and deployment of a global system for managing access control lists at Google  
18. [Monarch](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/d84ab6c93881af998de877d0070a706de7bec6d8.pdf): Architecture of Google’s in-memory time series database  
19. [Thrift](https://thrift.apache.org/static/files/thrift-20070401.pdf): Explore the design choices behind Facebook’s code-generation tool  
20. [Bitcoin](https://bitcoin.org/bitcoin.pdf): The ground-breaking introduction to the peer-to-peer electronic cash system  
21. [WTF - Who to Follow Service at Twitter](https://web.stanford.edu/~ashishg/papers/wtf_overview.pdf): Twitter’s (now X) user recommendation system  
22. [MyRocks](https://www.vldb.org/pvldb/vol13/p3217-matsunobu.pdf): LSM-Tree Database Storage Engine  
23. [GoTo Considered Harmful](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)  
24. [Raft Consensus Algorithm](https://raft.github.io/raft.pdf): Learn about the more understandable consensus algorithm  
25. [Time Clocks and Ordering of Events](https://lamport.azurewebsites.net/pubs/time-clocks.pdf): The extremely important paper that explains the concept of time and event ordering in a distributed system  

## Data Science (ML/NN)

### Free e-books

1. [Deep Learning](http://www.deeplearningbook.org/) - Ian Goodfellow, Yoshua Bengio, and Aaron Courville
2. [Mathematics for Machine Learning](https://mml-book.github.io/) - Marc Peter Deisenroth, A. Aldo Faisal, Cheng Soon Ong
3. [An Introduction to Statistical Learning](https://www.statlearning.com/) - Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani, Jonathan Taylor
4. [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/) - Jerome H. Friedman, Robert Tibshirani, and Trevor Hastie
5. [Probabilistic Machine Learning: An Introduction](https://probml.github.io/pml-book/) - Kevin Patrick Murphy
6. [Probabilistic Machine Learning: Advanced Topics](https://probml.github.io/pml-book/) - Kevin Patrick Murphy
7. [Understanding Machine Learning](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) - Shai Shalev-Shwartz and Shai Ben-David
8. [Automated Machine Learning](https://www.automl.org/book/) - Frank Hutter, Lars Kotthoff, Joaquin Vanschoren
9. [Applied Causal Inference](https://appliedcausalinference.github.io/aci_book/index.html) - Uday Kamath, Kenneth Graham, Mitchell Naylor
10. [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) - Richard S. Sutton and Andrew G. Barto
11. [The Hundred-Page Machine Learning Book](http://themlbook.com/) - Andriy Burkov
12. [Machine Learning Engineering](http://www.mlebook.com/wiki/doku.php) - Andriy Burkov
13. [Natural Language Processing with Python](https://www.nltk.org/book/) - Steven Bird, Ewan Klein, and Edward Loper
14. [Dive into Deep Learning](https://d2l.ai/) - Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola
15. [Machine Learning Yearning](https://github.com/ajaymache/machine-learning-yearning) - Andrew NG
16. [Machine Learning for Humans](https://vas3k.com/blog/machine_learning/) - Vishal Maini, Samer Sabri
17. [Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/people/cmbishop/#!prml-book) - Christopher M. Bishop
18. [Deep Learning on Graphs](https://yaoma24.github.io/dlg_book/index.html) - Yao Ma and Jiliang Tang
19. [Approaching (Almost) Any Machine Learning Problem](https://github.com/abhishekkrthakur/approachingalmost) - Abhishek Thakur
20. [Feature Engineering and Selection](https://bookdown.org/max/FES/) - Max Kuhn and Kjell Johnson
21. [Hands-On Machine Learning with R](https://bradleyboehmke.github.io/HOML/) - Bradley Boehmke & Brandon Greenwell
22. [Deep Learning Interviews](https://arxiv.org/abs/2201.00650) - Shlomo Kashani and Amir Ivry
23. [Machine Learning Interpretability](https://www.oreilly.com/library/view/an-introduction-to/9781492033158/) - Patrick Hall and Navdeep Gill
24. [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) - Christoph Molnar
25. [Boosting: Foundations and Algorithms](https://direct.mit.edu/books/oa-monograph/5342/BoostingFoundations-and-Algorithms) - Robert E. Schapire, Yoav Freund
26. [A Brief Introduction to Machine Learning for Engineers](https://arxiv.org/abs/1709.02840) - Osvaldo Simeone
27. [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) - Daniel Jurafsky & James Martin
28. [Computer Vision: Models, Learning, and Inference](https://udlbook.github.io/cvbook/) - Simon J.D. Prince
29. [Information Theory, Inference and Learning Algorithms](http://www.inference.org.uk/mackay/itila/) - David J. C. MacKay
30. [Machine Learning For Dummies](https://www.ibm.com/downloads/cas/GB8ZMQZ3) - Judith Hurwitz and Daniel Kirsch
31. [Algebra, Topology, Differential Calculus, and Optimization Theory for Computer Science and Machine Learning](https://www.cis.upenn.edu/~jean/gbooks/geomath.html)
32. [@mathtalent Lecture Notes](https://skim.math.msstate.edu/LectureNotes/)
33. [Mathematical Methods for Computer Vision, Robotics, and Graphics](http://graphics.stanford.edu/courses/cs205a-13-fall/assets/notes/cs205a_notes.pdf)

### github

1. [The Data Engineering Handbook](https://github.com/DataExpert-io/data-engineer-handbook)
1. [Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners)
1. [Machine Learning YouTube Videos](https://github.com/ujjwalkarn/Machine-Learning-Videos)
1. [Mathematics for Machine Learning](https://github.com/mml-book/mml-book.github.io)
1. [Deep Learning Book](https://github.com/janishar/mit-deep-learning-book-pdf)
1. [Machine Learning ZoomCamp](https://github.com/alexeygrigorev/mlbookcamp-code)
1. [Machine Learning Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials)
1. [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning)
1. [CS 229 Machine Learning Cheatsheets](https://github.com/afshinea/stanford-cs-229-machine-learning)
1. [Machine Learning Interview Guide](https://github.com/Sroy20/machine-learning-interview-guide)
1. [Awesome Production Machine Learning](https://github.com/EthicalML/awesome-production-machine-learning)
1. [365 Data Science Flashcards](https://365datascience.com/flashcards/)
1. [ref](https://www.kdnuggets.com/10-github-repositories-to-master-machine-learning?utm_source=rss&utm_medium=rss&utm_campaign=10-github-repositories-to-master-machine-learning) > [Virgilio](https://github.com/virgili0/Virgilio) | [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) | [Microsoft: 10 Weeks, 20 Lessons, Data Science](https://github.com/microsoft/Data-Science-For-Beginners) | [Data science Python notebooks](https://github.com/donnemartin/data-science-ipython-notebooks) | [📚 Papers & tech blog](https://github.com/eugeneyan/applied-ml) | [Open Source Data Science Masters](https://github.com/datasciencemasters/go) | [Awesome Data Science](https://github.com/academic/awesome-datascience) | [Data science interview questions and answers](https://github.com/alexeygrigorev/data-science-interviews) | [free self-taught education in Data Science!](https://github.com/ossu/data-science)
1. [data science project template](https://github.com/drivendataorg/cookiecutter-data-science)
1. [labml.ai Deep Learning Paper Implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations): 60+ Implementations/tutorials of deep learning papers with side-by-side notes
1. [Deep Learning Models](https://github.com/rasbt/deeplearning-models): A collection of various deep learning architectures, models, and tips
1. [fastai book](https://github.com/fastai/fastbook): The fastai book, published as Jupyter Notebooks

- [ref](https://newsletter.theaiedge.io/p/30-free-machine-learning-e-books)

## Terminology and Comparisons

- See [Glossary.md](Glossary.md): an overview of key terminology, definitions, and comparisons between related concepts.
