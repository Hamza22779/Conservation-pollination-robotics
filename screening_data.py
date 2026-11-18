import os
from _paths import DATA, FIGS
# Screening ledger for the systematic map (OpenAlex title searches, run 18 Nov 2026)
# plus records added from other sources (prior evidence library / citation chasing).
# Codes: D direct empirical pollination action; E enabling/prototype/simulation; R review/commentary/news;
#        O other robotics/drones relevant to pollinator or plant conservation; X out of scope;
#        U insufficient metadata; DUP duplicate.
# For D records: crop | taxon class | setting | platform | mechanism
import csv

Q1 = "OpenAlex title.search 'robot pollination' (n=117)"
Q2 = "OpenAlex title.search 'drone pollination' (n=70)"
Q3 = "OpenAlex title.search 'UAV pollination' (n=21)"
Q4 = "OpenAlex title.search 'autonomous pollination' (n=84)"
OS = "Other sources (prior library / citation chasing)"

R = []
def add(src, yr, title, doi, code, crop="", tclass="", setting="", platform="", mech="", note=""):
    R.append(dict(source=src, year=yr, title=title, doi=doi, code=code, crop=crop, taxon_class=tclass,
                  setting=setting, platform=platform, mechanism=mech, note=note))

# ---------------- Q1 robot pollination ----------------
add(Q1,2023,"Robotic Pollination of Apples in Commercial Orchards","10.32388/bb494v","D","Apple","Fruit tree","Open field","Ground manipulator","Electrostatic spray")
add(Q1,2017,"Sticky Solution Provides Grip for the First Robotic Pollinator","10.1016/j.chempr.2017.01.012","R")
add(Q1,2017,"Robotic Pollination - Targeting kiwifruit flowers for commercial application","hdl:10289/11803","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2023,"Robotic Pollinating Tools for Actinidia Crops","10.3390/iecag2023-16279","E")
add(Q1,2024,"A novel redundant cooperative control strategy for robotic pollination","10.1016/j.compag.2024.108846","E")
add(Q1,2025,"AI-Integrated Robotic Pollinator for Sustainable Agriculture","10.1007/978-3-032-03751-0_33","U")
add(Q1,2018,"Detection of Partially Occluded Flowers for Robotic Pollination","","E")
add(Q1,2024,"An Approach for Robotic Pollination that Utilizes Imitation Learning","10.33915/etd.12599","E")
add(Q1,2023,"Capsicum Flower Identification for Robotic Pollination in Greenhouses","10.1109/icmlc58545.2023.10327967","E")
add(Q1,2021,"Real-time detection of kiwifruit flower and bud simultaneously in orchard using YOLOv4 for robotic pollination","10.1016/j.compag.2021.106641","E")
add(Q1,2024,"Design and Implementation of an Innovative Soft Tool for Robotic Pollination","10.1109/robot61475.2024.10797408","D","Unspecified/surrogate","Surrogate target","Laboratory","Ground manipulator","Contact")
add(Q1,2023,"Robotic Pollination System for Chirimoya Plantations in the Huanuco Region","10.1109/intercon59652.2023.10326086","E")
add(Q1,2022,"Towards aerial robotic pollination for controlled crosses in Pinus taeda","10.13031/aim.202200677","E",note="forest-tree breeding; conservation-transferable")
add(Q1,2025,"Flower Cluster Matching Utilizing The Unscented Transform For Robotic Pollination","10.33915/etd.12812","E")
add(Q1,2021,"Replacing cheap nature? Sustainability, capitalist future-making and political ecologies of robotic pollination","10.1177/2514848620987368","R")
add(Q1,2025,"Vision-Guided Targeted Grasping and Vibration for Robotic Pollination in Controlled Environments","10.48550/arxiv.2510.06146","D","Pepper and tomato","Vegetable","Protected","Ground manipulator","Vibration")
add(Q1,2025,"Robotic Pollination in Greenhouse Farming: Current Innovations, Challenges, and Future Prospects","10.13005/ojc/410439","R")
add(Q1,2026,"Advancements and prospects in key technologies for robotic pollination in greenhouse pepper breeding: a review","10.3389/fpls.2026.1778541","R")
add(Q1,2024,"Small crop detection based on improved YOLOv8 algorithm for robotic pollination","10.1117/12.3050413","E")
add(Q1,2024,"Evaluation of Robotic Pollination for Strawberry Production in a Plant Factory with Artificial Lighting","10.20776/900122935","D","Strawberry","Berry","Protected","Ground manipulator","Contact")
add(Q1,2026,"CFPR-YOLO: chili flower pose estimation for robotic pollination in unstructured environments","10.3389/fpls.2026.1861155","E")
add(Q1,2024,"Learning to Improve Operational Efficiency from Pose Error Estimation in Robotic Pollination","10.3390/electronics13153070","E")
add(Q1,2019,"System designed to enable scientific analysis on robot pollination algorithm for orchard robot research","10.23919/elinfocom.2019.8706475","E")
add(Q1,2024,"Towards Autonomous, Aerial Pollination: Design of a Robotic Pollinator Payload for Controlled Crosses in Loblolly Pine","10.13031/aea.15916","E",note="forest-tree breeding; conservation-transferable")
add(Q1,2025,"Towards Closing the Loop in Robotic Pollination for Indoor Farming Via Autonomous Microscopic Inspection","10.1109/icra55743.2025.11127933","D","Strawberry","Berry","Protected","Ground manipulator","Vibration")
add(Q1,2025,"Robotic Pollination Through Airflow and Pose Estimation: A Non-Contact Approach for Precision Agriculture","10.2139/ssrn.5518711","E")
add(Q1,2022,"Artificial pollination of date palm (Phoenix dactylifera L.) using a platform mounted robotic pollination system (drone)","10.17660/actahortic.2022.1342.42","D","Date palm","Palm","Open field","Aerial (UAV)","Liquid spray")
add(Q1,2026,"Dual-scale flower detection and homography-guided cluster matching for robotic pollination in trellised kiwifruit orchards","10.1016/j.biosystemseng.2026.104561","E")
add(Q1,2026,"YOLOv8-PnP fusion architecture for non-contact robotic pollination","10.3389/fpls.2026.1771732","D","Tomato","Vegetable","Protected","Ground manipulator","Airflow")
add(Q1,2026,"Toward robotic pollination in greenhouse: Active eye-in-hand RGB-D vision for cucumber flowers","10.2139/ssrn.7564968","E")
add(Q1,2018,"Design of an Autonomous Precision Pollination Robot","10.1109/iros.2018.8594444","D","Bramble","Berry","Protected","Ground manipulator","Contact")
add(Q1,2019,"Autonomous pollination of individual kiwifruit flowers: Toward a robotic kiwifruit pollinator","10.1002/rob.21861","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2022,"Design of a lightweight robotic arm for kiwifruit pollination","10.1016/j.compag.2022.107114","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2025,"AUTOMATED POLLINATION ROBOTS","10.34132/mspc2025.01.06.37","U")
add(Q1,2019,"Flower Interaction Subsystem for a Precision Pollination Robot","10.1109/iros40897.2019.8967752","D","Bramble","Berry","Protected","Ground manipulator","Contact")
add(Q1,2025,"A comprehensive review of current robot-based pollinators for crop pollination","10.1007/s10462-025-11409-1","R")
add(Q1,2023,"The Robot Who Wants To Be A Pollinator","10.1145/3563657.3596055","R")
add(Q1,2021,"Modeling and Control of a Pollinator Flying Robot","10.1109/icrom54204.2021.9663526","E")
add(Q1,2019,"Robots for Kiwifruit Harvesting and Pollination","","R")
add(Q1,2018,"Novo-crafters - Robots for Pollination","","U")
add(Q1,2016,"An autonomous pollination robot for hormone treatment of tomato flower in greenhouse","10.1109/icsai.2016.7810939","D","Tomato","Vegetable","Protected","Ground manipulator","Liquid spray")
add(Q1,2021,"Evaluating the Quality of Kiwifruit Pollinated with an Autonomous Robot","10.55417/fr.2021009","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2023,"Shape classification technology of pollinated tomato flowers for robotic implementation","10.1038/s41598-023-27971-z","E")
add(Q1,2022,"Identification of the operating position and orientation of a robotic kiwifruit pollinator","10.1016/j.biosystemseng.2022.07.014","E")
add(Q1,2018,"Robotic bees for crop pollination: Why drones cannot replace biodiversity","10.1016/j.scitotenv.2018.06.114","R")
add(Q1,2024,"A Suspended Pollination Robot With a Flexible Multi-Degrees-of-Freedom Manipulator for Self-Pollinated Plants","10.1109/access.2024.3469784","D","Tomato","Vegetable","Protected","Suspended/rail/gantry","Vibration")
add(Q1,2022,"Seri Robot Manipulatorunde Ters Kinematik ... Cicek Tozlasma Algoritmasi","10.21597/jist.978481","X")
add(Q1,2022,"Automated Monitoring of Pollinators With Agricultural Robots","10.1109/icara55094.2022.9738573","O")
add(Q1,2025,"A vision-based robotic system for precision pollination of apples","10.1016/j.compag.2025.110158","D","Apple","Fruit tree","Open field","Ground manipulator","Electrostatic spray")
add(Q1,2024,"Design of Stickbug: a Six-Armed Precision Pollination Robot","10.1109/iros58592.2024.10801406","D","Bramble (artificial plants)","Surrogate target","Protected","Ground manipulator","Contact")
add(Q1,2011,"Design of control policies for spatially inhomogeneous robot swarms with application to commercial pollination","10.1109/icra.2011.5980440","E")
add(Q1,2021,"Design and Manufacture of an Aerial Pollinator Robot for Walnut Trees","10.1109/icrom54204.2021.9663500","D","Walnut","Nut tree","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q1,2025,"An Efficient Obstacle-Aware Pollination Robot System","10.1109/icia64617.2025.11277987","E")
add(Q1,2025,"Robotic cross-pollination of genetically modified flowers","10.1126/scirobotics.aed6762","R")
add(Q1,2024,"Pollinationbots - A Swarm Robotic System for Tree Pollination","10.1007/978-3-031-73503-5_8","E")
add(Q1,2008,"A Robotic Prototype for Spraying and Pollinating Date Palm Trees","10.1115/esda2008-59208","E")
add(Q1,2021,"A Robot Calibration Method Using a Neural Network Based on a Butterfly and Flower Pollination Algorithm","10.1109/tie.2021.3073312","X")
add(Q1,2020,"Design of a sensing module for a kiwifruit flower pollinator robot","10.48550/arxiv.2006.08045","E")
add(Q1,2019,"Localization Algorithm Design and Evaluation for an Autonomous Pollination Robot","10.33012/2019.17099","E")
add(Q1,2019,"Robotic Path Planning Using Flower Pollination Algorithm","10.2174/2213275911666190320160837","X")
add(Q1,2026,"Robotics for Crop Pollination: Recent Advances and Future Direction","10.1002/rob.70343","R")
add(Q1,2025,"Engineering crop flower morphology facilitates robotization of cross-pollination and speed breeding","10.1016/j.cell.2025.07.028","D","Soybean and tomato (breeding)","Field crop","Protected","Ground manipulator","Contact")
add(Q1,2026,"AGRICAM: A Track-Mounted Crop Pollination Monitoring Robot","10.48550/arxiv.2608.29237","O")
add(Q1,2017,"Implementation of automated vanilla pollination robotic crane prototype","10.1109/sysose.2017.7994929","E",note="orchid crop; hand pollination obligatory outside native range")
add(Q1,2013,"A vision feedback robotic docking crane system with application to vanilla pollination","10.1504/ijaac.2013.055096","E")
add(Q1,2018,"An Overview of Perception Methods for Horticultural Robots: From Pollination to Harvest","10.48550/arxiv.1807.03124","R")
add(Q1,2025,"Towards Autonomous Strawberry Pollination via IoT and Robotics","10.1109/icac69156.2025.11361500","E")
add(Q1,2023,"A novel pollination robot for kiwifruit flower based on preferential flowers selection and precisely target","10.1016/j.compag.2023.107762","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2025,"Design and performance verification of an intelligent pollination robot for facility tomatoes","10.1016/j.compag.2025.111139","D","Tomato","Vegetable","Protected","Ground manipulator","Vibration")
add(Q1,2024,"Development of a Flexible Multi-Degrees-of-Freedom Robot for Plant Pollination","10.1109/sii58957.2024.10417630","E")
add(Q1,2024,"Robot Path Planning and Tracking with the Flower Pollination Search Optimization Algorithm","10.69996/jcai.2024020","X")
add(Q1,2025,"YOLOv8-based Agricultural Robots for Precision Pollination and Yield Prediction","10.1109/icscn67106.2025.11308389","U")
add(Q1,2024,"Automated Pollination and Crop Monitoring Using Robotics in Greenhouse Ecosystems","","U")
add(Q1,2025,"A Review on the Effectiveness of the Wyss Institute's Autonomous Flying Robots for Pollination","10.47611/jsrhs.v14i1.8534","R")
add(Q1,2013,"Proposal of Robot Support System 'mao' for Amaou Pollination","10.1299/jsmekyushu.2013.66.67","E")
add(Q1,2020,"Development of a micro aerial vehicle flying robot for automatic pollinating","","U")
add(Q1,2019,"Optimum Dynamic Analysis of a Robot Arm Using Flower Pollination Algorithm","10.1201/9780429021596-13","X")
add(Q1,2016,"Flowering plants pollination robotic system for greenhouses by means of nano copter (drone aircraft)","10.1109/itmqis.2016.7751907","E")
add(Q1,2018,"Trajectory planning of a robot arm using flower pollination algorithm","","X")
add(Q1,2025,"Towards Autonomous Raised Bed Flower Pollination with IoT and Robotics","10.3390/ecsa-12-26572","D","Raised-bed flowers (unspecified)","Vegetable","Protected","Ground manipulator","Contact")
add(Q1,2024,"Wearable Sensors Assess the Effects of Human-Robot Collaboration in Simulated Pollination","10.3390/s24020577","X")
add(Q1,2008,"Stabilization of a mobile robotic arm for precise spraying and pollinating in tall trees","","E")
add(Q1,2023,"An evaluation of pollination methods for strawberries cultivated in plant factories: robot vs hand","10.48130/tih-2023-0019","D","Strawberry","Berry","Protected","Ground manipulator","Contact")
add(Q1,2011,"Optimization of stochastic strategies for spatially inhomogeneous robot swarms: commercial pollination","10.1109/iros.2011.6094771","E")
add(Q1,2026,"Design and Implementation of a Mobile Robot System for Strawberry Flower Recognition and Pollination","10.5391/jkiis.2026.36.5.497","E")
add(Q1,2026,"Development of a Soft Robotic Tendon-Driven Arm for Extraterrestrial Precision Pollination","10.1109/aiiot68874.2026.11569524","E")
add(Q1,2026,"Path Planning of Pear Flower Pollination Robot Arm Based on DDPG","10.1007/978-981-95-4875-0_7","E")
add(Q1,2021,"Adaptive Flower Pollination Algorithm-Based Energy Efficient Routing Protocol for Multi-Robot Systems","10.1109/access.2021.3086628","X")
add(Q1,2024,"Evaluation of Biomechanical and Mental Workload During Human-Robot Collaborative Pollination Task","10.1177/00187208241254696","X")
add(Q1,2020,"Mobile Robot Path Planning Using a Flower Pollination Algorithm-Based Approach","10.1007/978-981-15-1842-3_6","X")
add(Q1,2022,"Optimal Flower Pollination Based Nonlinear PID Controller for Pantograph Robot Mechanism","10.18178/ijmerr.11.8.622-630","X")
add(Q1,2025,"Design and Optimization of Target Detection and 3D Localization Models for Intelligent Muskmelon Pollination Robots","10.3390/horticulturae11080905","E")
add(Q1,2012,"Hypercomplex number based automated robotic vanilla pollination system with vision sensing","","E")
add(Q1,2026,"Target Selection Based on Flower Cluster Topology for Robotic Pear Flower Pollination","10.1109/tafe.2026.3742683","E")
add(Q1,2018,"Optimization of Membership Function Parameters for Fuzzy Controllers ... Flower Pollination Algorithm","10.14313/jamris_1-2018/6","X")
add(Q1,2011,"Optimization of stochastic strategies for spatially inhomogeneous robot swarms (duplicate record)","10.1109/iros.2011.6048378","DUP")
add(Q1,2024,"Pioneering Business with the World's First Strawberry Pollination by Robots (HarvestX)","10.7210/jrsj.42.761","R")
add(Q1,2017,"The Design of Apple Artificial Pollination Welfare Robot by A Survey for the Elders' Needs of Rural Region","10.21288/resko.2017.11.4.357","R")
add(Q1,2025,"Clip-assisted flower detection and wind-compensated precision liquid pollination robot for kiwifruit orchards","10.1016/j.compag.2025.111250","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2025,"Economic benchmarking of assisted pollination methods for kiwifruit flowers: cost-effectiveness of robotic solution","10.1016/j.agsy.2025.104541","O")
add(Q1,2023,"A search and rescue robot search method based on flower pollination algorithm and Q-learning","10.1371/journal.pone.0283751","X")
add(Q1,2026,"Data and Code for: Micro-robots for the study of plant-pollinator interactions","10.6084/m9.figshare.32665950","O")
add(Q1,2022,"A Neural Network Structure ... for Tomato Flowering Phase Detection in Pollination Robots","10.3390/machines10111076","E")
add(Q1,2019,"Variable-dimensional Flower Pollination obstacle avoidance algorithm on NAO robot","10.1080/01691864.2019.1633954","X")
add(Q1,2025,"A Novel Multinozzle Targeting Pollination Robot for Clustered Kiwifruit Flowers Based on Air-Liquid Dual-Flow Spraying","10.1002/rob.22499","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(Q1,2026,"Real-time feature recognition of cantaloupe flowers and buds in greenhouse for pollination robot","10.1117/12.3096309","E")
add(Q1,2026,"Hierarchical deep reinforcement learning for dual-arm robotic pear blossom pollination","10.1016/j.compag.2026.112546","E")
add(Q1,2025,"Development of a Dual-Function Micro-Robotic System for Pollination and Nectar Collection","10.13140/rg.2.2.34116.90246","U")
add(Q1,2025,"Vertical farms and pollination robots: new technologies to supplement crop production","10.1007/s43538-025-00577-x","R")
add(Q1,2025,"A bi-objective discrete flower pollination algorithm for planning collaborative disassembly","10.1016/j.asoc.2025.113213","X")
add(Q1,2026,"Agricultural Pollination Innovation: Robotic Bees for Hass Avocado Cultivation in Colombia","10.5171/2025.4630125","R")
add(Q1,2025,"Knowledge-based evolutionary algorithm for task assignment of pollination robots and spraying drones","10.1016/j.eswa.2025.127408","E")
add(Q1,2024,"Autonomous Pollination System for Tomato Plants in Greenhouses on Edge Device","10.1109/iciset62123.2024.10939425","E")
add(Q1,2026,"Constrained Pole Placement Optimization Using the Flower Pollination Algorithm","10.48084/etasr.18761","X")
add(Q1,2025,"Flower detection using computer vision and 3D mapping for automatic pollination using robotic platform","10.17660/actahortic.2025.1433.31","E")
add(Q1,2026,"Development of a Robotic Platform for Pollination of Garden Strawberry in City-Farm Conditions","10.1007/978-3-032-35010-7_22","E")
add(Q1,2026,"Stereo-vision-based fruiting-shoot diameter estimation for robotic selective pollination in kiwifruit","10.1016/j.eja.2026.128321","E")

# ---------------- Q2 drone pollination ----------------
add(Q2,2020,"Drone Pollination","","U")
add(Q2,2021,"Autonomous Drone Pollination","","U")
add(Q2,2022,"Impact of Autonomous Drone Pollination in Date Palms","10.53894/ijirss.v5i4.732","D","Date palm","Palm","Open field","Aerial (UAV)","Liquid spray")
add(Q2,2021,"Drone Pollination of Flowering Vegetation for Agricultural Applications","10.1115/imece2021-70545","E")
add(Q2,2026,"Measurement of Strawberry Flower Displacement for Automated Drone Pollination","10.3173/air.35.105","E")
add(Q2,2026,"Field validation of an autonomous electrostatic drone pollination system for Japanese pear","10.1016/j.atech.2026.102108","D","Japanese pear","Fruit tree","Open field","Aerial (UAV)","Electrostatic spray")
add(Q2,2017,"E-Green Revolution: Intentional Pollination using Intelligent Agent Based Autonomous Drone-Pollinator-Bees","10.18782/2320-7051.5387","R")
add(Q2,2018,"Breeding system and bumblebee drone pollination of Meliosma tenuis","10.1111/plb.12699","X")
add(Q2,2023,"Efecto del vuelo de un dron sobre la polinizacion de cultivo de fresa en casa sombra","10.63728/riisds.v9i1.124","D","Strawberry","Berry","Protected","Aerial (UAV)","Dry pollen / airflow")
add(Q2,2021,"Pollination with drones: A successful response to the decline of entomophiles pollinators?","10.17268/sci.agropecu.2021.055","R")
add(Q2,2022,"Autonomous Visual Navigation for a Flower Pollination Drone","10.3390/machines10050364","E")
add(Q2,2010,"The pollination potential of bumblebee drones","10.25673/439","X")
add(Q2,2018,"Robotic bees for crop pollination: Why drones cannot replace biodiversity","10.1016/j.scitotenv.2018.06.114","DUP")
add(Q2,2022,"Novel Pollination Drone for Agricultural Assistance","10.22214/ijraset.2022.44596","U")
add(Q2,2025,"Drone Photographs of Pollinators in the Uppsala Region","10.5878/8f6x-6c31","O")
add(Q2,2017,"Could this pollinating drone replace butterflies and bees? (news)","10.1126/science.aal0730","R")
add(Q2,2024,"Artificial Pollination by Nano drone Technology: A review","10.33545/2618060x.2024.v7.i2g.2783","R")
add(Q2,2025,"Development of Pear Pollination System Using Autonomous Drones","10.3390/agriengineering7030068","D","Japanese pear","Fruit tree","Open field","Aerial (UAV)","Electrostatic spray")
add(Q2,2026,"AI-enabled drones for date palm pollination","10.1038/s41598-026-39739-2","D","Date palm","Palm","Open field","Aerial (UAV)","Liquid spray")
add(Q2,2021,"Could this pollinating drone replace butterflies and bees? (news, duplicate)","10.1126/article.2355386","DUP")
add(Q2,2021,"Could this pollinating drone replace butterflies and bees? (news, duplicate)","10.1126/article.2354208","DUP")
add(Q2,2019,"The potential management of the drone fly (Eristalis tenax) as a crop pollinator in New Zealand","10.30843/nzpp.2019.72.304","X")
add(Q2,2022,"Remote Sensing of Floral Resources for Pollinators - New Horizons From Satellites to Drones","10.3389/fevo.2022.869751","O")
add(Q2,2025,"Development and Testing of a Wind-Pollination Drone for Greenhouse Tomatoes","10.13031/aim.202500033","D","Tomato","Vegetable","Protected","Aerial (UAV)","Dry pollen / airflow")
add(Q2,2022,"Innovative and Effective Spray Method for Artificial Pollination of Date Palm Using Drone","10.21273/hortsci16739-22","D","Date palm","Palm","Open field","Aerial (UAV)","Liquid spray")
add(Q2,2023,"A novel approach for surveying flowers as a proxy for bee pollinators using drone images","10.1016/j.ecolind.2023.110123","O")
add(Q2,2023,"Flower Detection in Automatic Pollination System Using Drone","10.1299/jsmermd.2023.2a2-a26","E")
add(Q2,2021,"A study of a small drone of motion-simulated of pollinating bees","","U")
add(Q2,2017,"Pollinating drones and bee whoops have scientists buzzing (news)","10.1021/cen-09510-newscripts","R")
add(Q2,2023,"Polybee: Using Autonomous Micro-Drones to Boost Pollination","10.1142/9789811267918_0006","R")
add(Q2,2022,"Pollination System for Greenhouse Flowering Plants Using Nano Drones","10.1007/978-981-16-9613-8_15","E")
add(Q2,2023,"Drone Flight Experiment using RTK Positioning for Pear Pollination","10.1109/icce-taiwan58799.2023.10226794","E")
add(Q2,2025,"Enhanced SHADE for Drone Control in a Swarm-Intelligent Pollination System","10.2299/jsp.29.123","E")
add(Q2,2025,"Residual vibration control of artificial pollination sprayer for onboard drones","10.1299/mel.25-00031","E")
add(Q2,2016,"Flowering plants pollination robotic system for greenhouses by means of nano copter (duplicate)","10.1109/itmqis.2016.7751907","DUP")
add(Q2,2020,"Drone-delivered soap bubbles could help pollinate flowers (news)","10.1126/science.abd3878","R")
add(Q2,2023,"Autonomous Drone-Based Pollination System Using AI Classifier to Replace Bees for Greenhouse Tomato Cultivation","10.1109/access.2023.3312151","D","Tomato","Vegetable","Protected","Aerial (UAV)","Dry pollen / airflow")
add(Q2,2026,"Analysis of drone-assisted liquid pollinating effects in chestnut trees","10.13925/j.cnki.gsxb.20250260","D","Chestnut","Nut tree","Open field","Aerial (UAV)","Liquid spray")
add(Q2,2021,"A study on classification of pollination flowers using bee type drones","","U")
add(Q2,2022,"Perception, Path Planning, and Flight Control for a Drone-Enabled Autonomous Pollination System","10.3390/robotics11060144","E")
add(Q2,2022,"Artificial pollination of date palm using a platform mounted robotic pollination system (drone) (duplicate)","10.17660/actahortic.2022.1342.42","DUP")
add(Q2,2020,"C-Band Telemetry of Insect Pollinators Using a Miniature Transmitter and a Self-Piloted Drone","10.1109/tmtt.2020.3034323","O")
add(Q2,2022,"Measurement of Vibration Propagation Characteristics in Tomato Plants for Artificial Pollination by Drone","10.1299/jsmebiofro.2022.33.2b12","E")
add(Q2,1991,"Oriental orchid (Cymbidium pumilum) attracts drones of the Japanese honeybee","10.1007/bf01918392","X")
add(Q2,2025,"Optimized Yolov5s-Im for real-time apple flower detection in drone-based pollination","10.1016/j.atech.2025.101150","E")
add(Q2,2023,"Epidemic communication control methods suitable for inter-drone relay in pollination systems","10.1587/comex.2023xbl0013","E")
add(Q2,2025,"Effects of drone-assisted artificial pollination on fruit set and characteristics in Asian pear","10.1080/14620316.2025.2529849","D","Asian pear","Fruit tree","Open field","Aerial (UAV)","Liquid spray")
add(Q2,2024,"Lightweight and Robust YOLOv5s with MobileNetV3 and GhostNet for Precision Apple Flower Detection for Pollination Drones","10.1007/978-981-97-7778-5_4","E")
add(Q2,2026,"AI-Enabled Drone-Based Precision Pollination System for Palm Tree Orchards","10.1109/tia.2026.3722124","E")
add(Q2,2026,"Beyond Tractors and Ploughs: Pollinating the Future with AI and Nano-Drones in Indian Farming","10.52151/aet2026501.1913","R")
add(Q2,2024,"Evaluation method and design of greenhouse pear pollination drones based on grounded theory","10.1371/journal.pone.0311297","E")
add(Q2,2025,"AI-Enhanced Precision Pollination Techniques Integrating Drone Swarms and Plant Phenology Data","10.1109/icaft66710.2025.11452704","E")
add(Q2,2024,"Flight tracking control of mini-drone: Flower pollination algorithm based model-free control","10.1177/09544100241291189","X")
add(Q2,2024,"Remote-Controlled Drone-Based Spray Pollination System for Greenhouse Bitter Gourd Cultivation","10.47001/irjiet/2024.806014","D","Bitter gourd","Vegetable","Protected","Aerial (UAV)","Liquid spray")
add(Q2,2024,"Is the Artificial Pollination of Walnut Trees with Drones Able to Minimize Xanthomonas arboricola pv. juglandis? A Review","10.3390/app14072732","R")
add(Q2,2024,"Three-dimensional path planning and collision-free flight control for drone-assisted autonomous pollination systems","10.1139/dsa-2023-0105","E")
add(Q2,2025,"Evaluation of Electrostatic Spraying Performance for Drone-Based Pollination: Fruit Set Comparison","10.2139/ssrn.5367202","D","Japanese pear","Fruit tree","Open field","Aerial (UAV)","Electrostatic spray")
add(Q2,2025,"Optimizing drone-based pollination method ... for complex durian orchards","10.1038/s41598-025-04370-0","E")
add(Q2,2025,"Knowledge-based evolutionary algorithm for task assignment (duplicate)","10.1016/j.eswa.2025.127408","DUP")
add(Q2,2025,"Cluster-Based Flight Path Construction for Drone-Assisted Pear Pollination Using RGB-D Image Processing","10.3390/drones9070475","E")
add(Q2,2025,"Autonomous Drone-Based Pollination Systems for Enhancing Crop Yield in Orchards Using IoT and ML","10.1051/shsconf/202521601056","U")
add(Q2,2024,"Evaluations of drone based pesticide spraying effects on pollinators and natural enemies in brinjal","10.33545/26174693.2024.v8.i10r.2768","O")
add(Q2,2025,"Autonomous Drone-Based Pollination Systems ... (duplicate pdf record)","10.1051/shsconf/202521601056/pdf","DUP")
add(Q2,2023,"The golden native drone fly (Eristalinus punctulatus) is an effective hybrid carrot pollinator","10.1002/2688-8319.12290","X")
add(Q2,2016,"Field activities, active flying time and drones mating flight of Apis cerana","","X")
add(Q2,2026,"From Floral Contact to Biological Success: Plithogenic Mathematics ... Pollinating Drone Swarms","10.5281/zenodo.21893773","X")
add(Q2,2023,"Review for 'The golden native drone fly ...'","10.1002/2688-8319.12290/v1/review1","X")
add(Q2,2023,"Author response for 'The golden native drone fly ...'","10.1002/2688-8319.12290/v2/response1","X")
add(Q2,2023,"Decision letter for 'The golden native drone fly ...' (v2)","10.1002/2688-8319.12290/v2/decision1","X")
add(Q2,2023,"Decision letter for 'The golden native drone fly ...' (v1)","10.1002/2688-8319.12290/v1/decision1","X")

# ---------------- Q3 UAV pollination ----------------
add(Q3,2022,"Pollination Parameter Optimization and Field Verification of UAV-Based Pollination of 'Kuerle Xiangli'","10.3390/agronomy12102561","D","Pear (Korla fragrant)","Fruit tree","Open field","Aerial (UAV)","Liquid spray")
add(Q3,2019,"Study on Assistant Pollination of Facility Tomato by UAV","10.13031/aim.201900055","D","Tomato","Vegetable","Protected","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2021,"Addressing Greenhouse's Lack of Natural Pollinators - A UAV-Based Artificial Pollination System","10.1109/dcoss52077.2021.00058","E")
add(Q3,2023,"UAV-Based Apple Flowers Pollination System","10.1007/978-981-99-6124-5_9","E")
add(Q3,2025,"Experimental Study on UAV-Assisted Pollination in Hybrid Rice","10.3390/drones9050327","D","Hybrid rice","Field crop","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2026,"Investigation of artificial pollination through UAV on date palm yield","10.55627/zoobotanica.004.01.1909","D","Date palm","Palm","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2026,"Parallel Execution of Task-Specific UAVs in Apple-Orchard Pollination","10.1109/icce-taiwan71481.2026.11652400","E")
add(Q3,2023,"A meta-heuristic optimization approach for optimizing cross-pollination using UAVs","10.1590/1413-7054202347008123","E")
add(Q3,2024,"Particle Flow Simulation of Artificial Pollination Sprayer Equipped in a Rotary-wing UAV","10.1299/jsmefed.2024.os03-05","E")
add(Q3,2025,"FLYING FOR POLLINATORS: UAV-based vegetation height and topography to predict pollinator abundance","","O")
add(Q3,2024,"Optimization of Application Parameters for UAV-Based Liquid Pollination in Pear Orchards: A Yield and Cost Perspective","10.3390/agronomy14092033","D","Pear","Fruit tree","Open field","Aerial (UAV)","Liquid spray")
add(Q3,2026,"Asymmetric Duct Design for Directional Airflow Delivery in UAV-Assisted Greenhouse Tomato Pollination","10.3390/agronomy16171726","E")
add(Q3,2026,"UAV-Precision pollination as a complementary strategy for pistachio orchards in new Mediterranean growing areas","10.2139/ssrn.7217435","D","Pistachio","Nut tree","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2022,"A UAV Based Artificial Pollination in Frost-Affected Walnut Orchard","10.15832/ankutbd.1163150","D","Walnut","Nut tree","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2025,"Field Schedule of UAV-Assisted Pollination for Hybrid Rice Based on CFD-DPM Coupled Simulation","10.3390/agriculture15171798","E")
add(Q3,2022,"Parallel Hybrid 2-Opt Flower Pollination Algorithm for Real-Time UAV Trajectory Planning","10.1051/itmconf/20224803007","X")
add(Q3,2025,"Design of greenhouse four seasons pear pollination UAV based on AHP-QFD-TRIZ","10.63313/ah.9023","E")
add(Q3,2019,"The fruit-xenia effects of Carya illinoensis pollination on C. cathayensis assisted by UAV","","D","Hickory (Carya cathayensis)","Nut tree","Open field","Aerial (UAV)","Dry pollen / airflow")
add(Q3,2026,"Thermal UAV assessment of microclimatic variation induced by meandering mowing and pollinator diversity","10.1016/j.ecoinf.2026.104140","O")
add(Q3,2024,"Autonomous Crop Pollination Using a Double-Flap UAV Integrated with Real-Time SLAM Technology","10.1007/978-3-031-70684-4_23","E")
add(Q3,2025,"Evaluation tools and methods to assess the impact of downwash airflow generated by agricultural UAVs","10.71883/8grh-p653","E")

# ---------------- Q4 autonomous pollination (non-duplicates only listed individually) -------------
dups_q4 = [
 "Autonomous pollination of individual kiwifruit flowers (duplicate)","An autonomous pollination robot for hormone treatment of tomato flower (duplicate)",
 "Localization Algorithm Design ... (duplicate)","Perception, Path Planning, and Flight Control ... (duplicate)",
 "Three-dimensional path planning ... (duplicate)","Autonomous Pollination System for Tomato Plants ... (duplicate)",
 "Design of an Autonomous Precision Pollination Robot (duplicate)","Autonomous Drone Pollination (duplicate)",
 "Autonomous Visual Navigation ... (duplicate)","Evaluating the Quality of Kiwifruit ... (duplicate)",
 "Impact of Autonomous Drone Pollination in Date Palms (duplicate)","Development of Pear Pollination System ... (duplicate)",
 "Towards Autonomous, Aerial Pollination: Loblolly Pine (duplicate)","Polybee (duplicate)",
 "Towards Autonomous Strawberry Pollination via IoT (duplicate)","E-Green Revolution (duplicate)",
 "Wyss Institute review (duplicate)","Autonomous Drone-Based Pollination System ... Tomato (duplicate)",
 "Towards Autonomous Raised Bed Flower Pollination (duplicate)","Field validation of an autonomous electrostatic drone (duplicate)",
 "Towards Closing the Loop ... (duplicate)","Optimization of Membership Function ... FPA (duplicate)",
 "Variable-dimensional Flower Pollination ... NAO (duplicate)","Autonomous Drone-Based Pollination Systems ... SHS (duplicate)",
 "Autonomous Drone-Based Pollination Systems ... SHS pdf (duplicate)","YOLOv8-PnP fusion (duplicate)",
 "Autonomous Crop Pollination Using a Double-Flap UAV (duplicate)"]
for t in dups_q4: add(Q4,None,t,"","DUP")
add(Q4,2024,"Path Planning of Autonomous Pollination Using Heredity Algorithm for Intelligent Agriculture","10.1007/978-981-99-8498-5_30","E")
add(Q4,2019,"Intelligent Autonomous Pollination for Future Farming - A Micro Air Vehicle Conceptual Framework","10.1109/access.2019.2937171","R")
add(Q4,2026,"Autonomous Pollination System Using Multi-Source Perception and Intelligent Decision-Making","10.1109/iscait69154.2026.11477253","E")
add(Q4,2024,"CNN-Based Identifying Gender of Kiwifruit Flowers in Autonomous Pollination for Future Farming","10.1007/978-981-99-8498-5_12","E")
add(Q4,2023,"Real-Time Feature Recognition of Cantaloupe Flowers and Buds ... for Autonomous Pollination","10.2139/ssrn.4673081","E")
add(Q4,2025,"Advancements in artificial pollination of crops: from manual to autonomous","10.1016/j.compag.2025.110067","R")
add(Q4,2025,"A comprehensive review of autonomous flower pollination techniques: Progress, challenges, and future directions","10.1016/j.compag.2025.110577","R")
add(Q4,2025,"AI-Pollinators for Blueberry Farming: Enhancing Cross-Pollination Efficiency Through Autonomous Systems","10.1109/iementech65115.2025.10959148","U")
add(Q4,2025,"An Autonomous Dual-Fan Pollination Device: Modeling, Trajectory Optimization and Distribution Analysis","10.38124/ijisrt/25mar1299","E")
add(Q4,2023,"Towards autonomous cross-pollination: Portable multi-classification system for tomato flowers","10.1016/j.atech.2023.100205","E")
# botanical 'autonomous (self-)pollination' and algorithm records -> X (counted individually)
botany = ["Autonomous pollination alleviates pollen limitation in endemic Cienfuegosia yucatanensis",
 "Benefits of autonomous selfing under unpredictable pollinator environments","Delayed autonomous self-pollination in Hibiscus laevis",
 "Geographical variation in autonomous self-pollination in Helleborus foetidus","Pollinators of gardens of UNAH (Honduras)",
 "Autonomous self-pollination in three Centaurium species","Self-compatibility and autonomous selfing in Iris versicolor",
 "Delayed autonomous selfing in Arthropodium cirratum","Floral longevity and autonomous selfing in Collinsia heterophylla",
 "Autonomous self-pollination in Pogonia minor","Autonomous self-pollination in Cymbidium (Orchidaceae)",
 "Corolla wilting and delayed selfing in Pedicularis dunniana","Autonomous self-pollination in Fabaceae (Argentina)",
 "Evolution of autonomous selfing in Schizanthus","Delayed autonomous self-pollination in Crotalaria micans",
 "Autonomous self-pollination in Impatiens hypophylla","Autonomous selfing vs population size in a monocarpic plant",
 "Sweat bee visitation and selfing in Cyrtosia septentrionalis","Autonomous self-pollination in Epipogium roseum",
 "Delayed selfing in Saxifraga hirculus","Autonomous self-pollination in Satyrium rupestre",
 "Premature pollen development and selfing in soybean","Autonomous self-pollination in Eulophia",
 "Prior autonomous selfing in Tillandsia multicaulis","Selfing and flower colour in Silene littorea",
 "Autonomous self-pollination and insect pollination in sesame","Autonomous selfing in Gentianopsis paludosa",
 "Floral scent and selfing in Arabis alpina","Autonomous self-pollination of Passiflora","Delayed selfing in Epipactis helleborine",
 "Prior autonomous self-pollination in a high-Andean orchid","Potential autonomous selfing in Gesneria citrina",
 "Pollinators and selfing in Banksia and Hakea invasions","Cremastra saprophytica new orchid species",
 "Pterygodium vermiferum new orchid species","Pollination biology of Gossypium turneri (endangered wild cotton)",
 "Inbreeding depression and selfing in rare Hibiscus taxon","Corrigendum high-Andean orchid",
 "Pollination syndromes and delayed selfing in Kenyan Hibiscus","Early autonomous selfing in Pitcairnia brittoniana",
 "Faculty Opinions recommendation (selfing)","Differences in pollination syndromes ... H. flavifolius (duplicate-type botany record)"]
for t in botany: add(Q4,None,t,"","X",note="botanical 'autonomous (self-)pollination'")
algo = ["FPA longitudinal control autonomous vehicle","Path planning AUV with FPA, GA and Q-learning",
 "FPA-optimized PID for autonomous hybrid power system","FPA for 31-level H-bridge PV inverter",
 "FPA for DC-link voltage regulation"]
for t in algo: add(Q4,None,t,"","X",note="metaheuristic 'flower pollination algorithm'")

# ---------------- Other sources ----------------
add(OS,2023,"Development and evaluation of precision liquid pollinator for kiwifruit","10.1016/j.compag.2023.108193","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(OS,2025,"Pollen deposition performance of an airflow-assisted targeted pollinating device for kiwi fruit flower","10.1016/j.biosystemseng.2025.01.010","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Airflow")
add(OS,2024,"Accurate and robust pollinations for watermelons using intelligence guided visual servoing","10.1016/j.compag.2024.108753","D","Watermelon","Vegetable","Protected","Ground manipulator","Contact")
add(OS,2023,"Delivery of pollen to forsythia flower pistils autonomously and precisely using a robot arm","10.1016/j.compag.2023.108274","D","Forsythia","Ornamental","Laboratory","Ground manipulator","Contact")
add(OS,2025,"Robust pollination for tomato farming using deep learning and visual servoing","10.1017/S0263574724001243","D","Tomato","Vegetable","Protected","Suspended/rail/gantry","Airflow")
add(OS,2017,"Materially engineered artificial pollinators","10.1016/j.chempr.2017.01.008","D","Japanese lily (Lilium japonicum)","Ornamental","Laboratory","Aerial (UAV)","Contact")
add(OS,2020,"Soap Bubble Pollination","10.1016/j.isci.2020.101188","D","Pear","Fruit tree","Open field","Aerial (UAV)","Liquid spray",note="bubble carrier")
add(OS,2024,"A new approach for artificial pollination in walnut trees: AirPoll","10.1016/j.jenvman.2024.122123","D","Walnut","Nut tree","Open field","Aerial (UAV)","Dry pollen / airflow")
add(OS,2023,"Experiment on Liquid Pollination of Pear Tree with Horizontal Scaffolding Based on Multi-rotor UAV","10.6041/j.issn.1000-1298.2023.S2.015","D","Pear","Fruit tree","Open field","Aerial (UAV)","Liquid spray")
add(OS,2023,"Effects of flight parameters of plant protection drone on pollination droplets and fruit setting of camellia","10.11975/j.issn.1002-6819.202306034","D","Oil camellia","Fruit tree","Open field","Aerial (UAV)","Liquid spray")
add(OS,2022,"Study on seed production and pollination of indica-japonica hybrid rice assisted by multi-rotor UAV","10.13733/j.jcam.issn.2095-5553.2022.09.004","D","Hybrid rice","Field crop","Open field","Aerial (UAV)","Dry pollen / airflow")
add(OS,2017,"Distribution law of rice pollen in the wind field of small UAV","10.25165/j.ijabe.20171004.3103","D","Hybrid rice","Field crop","Open field","Aerial (UAV)","Dry pollen / airflow")
add(OS,2017,"Automated pollination of kiwifruit flowers","10.5281/zenodo.895619","D","Kiwifruit","Vine fruit","Open field","Ground manipulator","Liquid spray")
add(OS,2022,"Collecting critically endangered cliff plants using a drone-based sampling manipulator","10.1038/s41598-022-17679-x","O")

with open(os.path.join(DATA, "screening_ledger.csv"),"w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(R[0].keys())); w.writeheader(); w.writerows(R)
print(len(R))
