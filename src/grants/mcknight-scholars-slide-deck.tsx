import React from 'react';

const SlideTitle = ({ children }) => (
  <div className="bg-gradient-to-r from-purple-800 to-purple-600 text-white p-6 rounded-t-lg">
    <h1 className="text-2xl font-bold">{children}</h1>
  </div>
);

const SlideContent = ({ children }) => (
  <div className="bg-white p-6 rounded-b-lg shadow-lg mb-6">
    {children}
  </div>
);

const Slide = ({ title, children }) => (
  <div className="mb-8">
    <SlideTitle>{title}</SlideTitle>
    <SlideContent>{children}</SlideContent>
  </div>
);

const BulletPoint = ({ children }) => (
  <div className="flex items-start mb-3">
    <div className="text-purple-600 font-bold mr-2 mt-1">•</div>
    <div>{children}</div>
  </div>
);

const McKnightScholarsSlides = () => {
  return (
    <div className="w-full max-w-4xl mx-auto">
      {/* Title Slide */}
      <div className="bg-gradient-to-r from-purple-900 to-purple-600 text-white p-8 rounded-lg shadow-lg mb-8 text-center">
        <h1 className="text-3xl font-bold mb-4">McKnight Scholars Award</h1>
        <h2 className="text-xl mb-6">Explainable NeuroAI for Neural Circuit Understanding</h2>
        <p className="italic">A Three-Year Research Proposal</p>
        <div className="mt-6 text-sm opacity-80">
          Prepared for: Mass General Brigham NeuroAI Center Interview
        </div>
      </div>

      {/* Overview Slide */}
      <Slide title="Award Overview">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Program Description</h3>
            <BulletPoint>Prestigious award for early-career neuroscientists</BulletPoint>
            <BulletPoint>Supports exceptional scientists establishing independent labs</BulletPoint>
            <BulletPoint>Emphasis on impactful neuroscience research</BulletPoint>
            <BulletPoint>Values diversity, equity, and inclusion in science</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Award Details</h3>
            <BulletPoint>$225,000 total funding over three years ($75,000/year)</BulletPoint>
            <BulletPoint>Flexible use of funds (equipment, salary, supplies, etc.)</BulletPoint>
            <BulletPoint>No indirect costs allowed</BulletPoint>
            <BulletPoint>10 awardees selected annually</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Eligibility Slide */}
      <Slide title="Eligibility & Timeline">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Eligibility Requirements</h3>
            <BulletPoint>Assistant Professors with less than 5 years at that rank</BulletPoint>
            <BulletPoint>At non-profit research institutions in U.S.</BulletPoint>
            <BulletPoint>Demonstrated commitment to inclusive lab environment</BulletPoint>
            <BulletPoint>Cannot be tenured or hold another McKnight award</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Key Dates (2026 Cycle)</h3>
            <div className="bg-purple-50 p-4 rounded-lg">
              <ul className="list-none">
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">August 2025:</span> 
                  <span>Application period opens</span>
                </li>
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">January 2026:</span> 
                  <span>Application deadline</span>
                </li>
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">April 2026:</span> 
                  <span>Finalist notifications</span>
                </li>
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">May 2026:</span> 
                  <span>Interviews</span>
                </li>
                <li className="flex">
                  <span className="w-32 font-semibold">July 1, 2026:</span> 
                  <span>Funding begins</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </Slide>

      {/* Research Proposal Slide */}
      <Slide title="Proposed Research">
        <h3 className="text-lg font-bold text-purple-700 mb-3">Neural Circuit Decoding through Explainable NeuroAI</h3>
        <div className="grid grid-cols-1 gap-4">
          <BulletPoint>
            <span className="font-semibold">Research Goal:</span> Develop neuroscience-informed AI architectures that reveal underlying neural circuit mechanisms while maintaining clinical interpretability.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Innovative Approach:</span> Create circuit-inspired attention mechanisms that mimic known neurological processes, enabling both improved predictions and mechanistic insights into brain function.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Technical Framework:</span> Implement dual-path neural networks where one path maximizes predictive performance while the second generates interpretable circuit models that neurologists can validate.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Clinical Applications:</span> Focus on neurological recovery mechanisms after acute brain injury, identifying circuit-level biomarkers that predict recovery trajectories.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Broader Impact:</span> Bridge the gap between "black box" AI systems and neurological mechanistic understanding, potentially transforming how we understand brain function and disease.
          </BulletPoint>
        </div>
      </Slide>

      {/* Specific Aims Slide */}
      <Slide title="Research Specific Aims">
        <div className="grid grid-cols-1 gap-6">
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Aim 1: Circuit-Inspired Neural Network Architecture</h3>
            <BulletPoint>Develop attention mechanisms modeled after known neural circuit principles</BulletPoint>
            <BulletPoint>Incorporate hierarchical processing inspired by brain structure</BulletPoint>
            <BulletPoint>Validate architecture on publicly available EEG datasets</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Aim 2: Mechanistic Interpretability Framework</h3>
            <BulletPoint>Create visualization tools that map model activations to neural circuit components</BulletPoint>
            <BulletPoint>Develop circuit reconstruction algorithms from model weights</BulletPoint>
            <BulletPoint>Test interpretations against existing neurophysiological knowledge</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Aim 3: Clinical Validation and Application</h3>
            <BulletPoint>Apply framework to predict recovery from traumatic brain injury and coma</BulletPoint>
            <BulletPoint>Identify circuit-level biomarkers predictive of outcomes</BulletPoint>
            <BulletPoint>Validate findings through clinical collaboration</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Alignment Slide */}
      <Slide title="Alignment with NeuroAI Center">
        <h3 className="text-lg font-bold text-purple-700 mb-3">Strategic Fit with Center's Mission</h3>
        <div className="grid grid-cols-1 gap-4">
          <BulletPoint>
            <span className="font-semibold">Research Synergy:</span> Directly complements Dr. Zabihi's work on EEG signal processing and Dr. Rosenthal's research on physiologic biomarkers for brain monitoring.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Explainable AI Focus:</span> Addresses the center's need for interpretable AI models that clinicians can understand and trust, especially in critical care settings.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Clinical Translation:</span> Practical applications align with MGH's clinical mission while advancing fundamental neuroscience understanding.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Collaborative Potential:</span> Leverages MGH's unique datasets and clinical expertise while bringing novel AI approaches to existing problems.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">DEI Commitment:</span> Proposal includes specific plans for inclusive lab environment and outreach, matching McKnight Foundation's increased emphasis on diversity.
          </BulletPoint>
        </div>
      </Slide>

      {/* Expanded Impact Slide */}
      <Slide title="Expected Outcomes & Impact">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Scientific Contributions</h3>
            <BulletPoint>Novel circuit-inspired neural network architectures</BulletPoint>
            <BulletPoint>Framework for extracting mechanistic insights from AI models</BulletPoint>
            <BulletPoint>New understanding of circuit mechanisms in recovery</BulletPoint>
            <BulletPoint>3-5 high-impact publications</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-purple-700 mb-3">Broader Impact</h3>
            <BulletPoint>Bridge between AI performance and neuroscientific understanding</BulletPoint>
            <BulletPoint>Improved clinical prognostication tools</BulletPoint>
            <BulletPoint>Open-source software and educational resources</BulletPoint>
            <BulletPoint>Mentorship of diverse trainees in NeuroAI</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* McKnight Community Slide */}
      <Slide title="McKnight Scholar Community">
        <div className="grid grid-cols-1 gap-4">
          <div className="mb-2">
            <p>The McKnight Scholar award provides not just funding, but access to a prestigious community of neuroscientists that continues throughout one's career:</p>
          </div>
          <BulletPoint>
            <span className="font-semibold">Annual Conference:</span> McKnight Scholars attend the annual McKnight Conference on Neuroscience for three years after receiving the award, then return every three years.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Networking Opportunities:</span> Connect with leading neuroscientists across career stages and research areas.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Collaborative Potential:</span> McKnight Scholars often develop cross-institutional research collaborations.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Career Development:</span> Senior McKnight Scholars provide mentorship and career guidance.
          </BulletPoint>
          <div className="mt-2 text-center text-purple-700 italic">
            "Most McKnight award winners will tell you that a huge benefit of receiving a McKnight award is the chance to join a community of the nation's best neuroscientists that they will continue to learn from, interact and collaborate with over their lifetime."
          </div>
        </div>
      </Slide>
    </div>
  );
};

export default McKnightScholarsSlides;