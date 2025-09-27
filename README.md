# Mars Helicopter Backup System  

## 📌 Project Synopsis  
This project proposes a **redundant backup system** for the Mars helicopter. Instead of overworking two identical systems at once, the design uses a **microcontroller unit (MCU) buffer** that collects real-time data and periodically syncs it with a backup system. If the primary system fails, the backup can immediately take over with minimal data loss, ensuring mission continuity.  

---

## 🎯 Research Objectives  
- Design a **dual-system architecture** for redundancy.  
- Implement an **MCU buffer** to handle real-time data transfer and synchronization.  
- Develop a **failover mechanism** to switch from the primary to the backup system seamlessly.  
- Simulate and validate system performance under different failure scenarios.  

---

## 🔬 Research Approach  
1. **System Design**  
   - Block diagram and architecture finalized by the Hardware Team.  
   - Defined communication interfaces between MCU, System 1, and System 2.  

2. **Software Development**  
   - MCU buffer logic coded (data collection → storage → synchronization).  
   - Failover detection and switching mechanism implemented.  

3. **Testing & Validation**  
   - Simulation of various failure scenarios (e.g., power failure, data corruption).  
   - Analysis of buffer efficiency and data integrity during failover.  

---

## 📊 Expected Results & Products  
- A **working simulation** of the redundant backup system.  
- A **poster and technical report** with diagrams, methodology, and results.  
- A **demo video** showcasing failover in action.  

---

## 🌍 Commercialization & Societal Impact  
- **Space Missions:** Improves reliability of aerial vehicles in extreme environments like Mars.  
- **Earth Applications:** Can be adapted for **drones, autonomous vehicles, and robotics** where reliability is critical.  
- **Broader Impact:** Demonstrates how redundancy can **reduce mission failure risks** and **extend system lifetime**.  

---

## 📅 Timeline  
- **Weeks 1–2:** System design finalized (Hardware).  
- **Weeks 3–4:** Failover simulation implemented (Software).  
- **Weeks 5–6:** Testing, validation, final poster/report, and demo.  

---

## 📂 Repository Structure  
