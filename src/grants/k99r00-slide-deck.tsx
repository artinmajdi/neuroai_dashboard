import React from 'react';

const SlideTitle = ({ children }) => (
  <div className="bg-gradient-to-r from-blue-800 to-blue-600 text-white p-6 rounded-t-lg">
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
    <div className="text-blue-600 font-bold mr-2 mt-1">•</div>
    <div>{children}</div>
  </div>
);

const K99R00Slides = () => {
  return (
    <div className="w-full max-w-4xl mx-auto">
      {/* Title Slide */}
      <div className="bg-gradient-to-r from-blue-900 to-blue-600 text-white p-8 rounded-lg shadow-lg mb-8 text-center">
        <h1 className="text-3xl font-bold mb-4">NIH BRAIN Initiative K99/R00</h1>
        <h2 className="text-xl mb-6">Pathway to Independence Award</h2>
        <p className="italic">A Funding Strategy for NeuroAI Research</p>
        <div className="mt-6 text-sm opacity-80">
          Prepared for: Mass General Brigham NeuroAI Center Interview
        </div>
      </div>

      {/* Overview Slide */}
      <Slide title="Overview & Purpose">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Program Description</h3>
            <BulletPoint>Facilitates transition from postdoctoral research to independent faculty position</BulletPoint>
            <BulletPoint>Two phases: mentored (K99) followed by independent research (R00)</BulletPoint>
            <BulletPoint>Special emphasis on diversity in NIH BRAIN Initiative version</BulletPoint>
            <BulletPoint>Focus on innovative approaches in NeuroAI</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Key Benefits</h3>
            <BulletPoint>Substantial funding: Up to $250,000/year during R00 phase</BulletPoint>
            <BulletPoint>Career stability during critical transition period</BulletPoint>
            <BulletPoint>Enhanced visibility within neuroscience community</BulletPoint>
            <BulletPoint>Protected research time (75% effort commitment)</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Eligibility Slide */}
      <Slide title="Eligibility & Requirements">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Eligibility Criteria</h3>
            <BulletPoint>Postdoctoral researchers with ≤5 years experience</BulletPoint>
            <BulletPoint>Must be in mentored position at application time</BulletPoint>
            <BulletPoint>U.S. citizenship not required for standard K99</BulletPoint>
            <BulletPoint>U.S. citizenship/permanent residency required for BRAIN diversity K99</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Application Components</h3>
            <BulletPoint>Research plan integrating K99 and R00 phases</BulletPoint>
            <BulletPoint>Career development plan</BulletPoint>
            <BulletPoint>Strong mentorship team with expertise in NeuroAI</BulletPoint>
            <BulletPoint>Institutional commitment letters</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Alignment Slide */}
      <Slide title="Alignment with NeuroAI Center">
        <h3 className="text-lg font-bold text-blue-700 mb-3">Strategic Alignment</h3>
        <div className="grid grid-cols-1 gap-4">
          <BulletPoint>
            <span className="font-semibold">Multimodal Data Integration:</span> My proposed K99/R00 would focus on developing transformer-based architectures for integrating EEG, EHR, and neuroimaging data—directly supporting Dr. Zabihi's work on HyperEnsemble learning.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Explainable AI:</span> Will incorporate SHAP values and attention mechanisms to make models interpretable for clinicians, addressing a key center priority.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Clinical Translation:</span> Focuses on prognostic models for coma recovery, aligning with Dr. Rosenthal's clinical research priorities.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Institutional Strength:</span> MGH's strong NIH funding track record enhances competitiveness for this award.
          </BulletPoint>
        </div>
      </Slide>

      {/* Timeline Slide */}
      <Slide title="Timeline & Strategy">
        <div className="grid grid-cols-1 gap-6">
          <div className="mb-4">
            <h3 className="text-lg font-bold text-blue-700 mb-3">Key Dates</h3>
            <div className="bg-blue-50 p-4 rounded-lg">
              <ul className="list-none">
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">Feb 13, 2025:</span> 
                  <span>Next standard application deadline</span>
                </li>
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">June 13, 2025:</span> 
                  <span>BRAIN Initiative diversity K99/R00 deadline</span>
                </li>
                <li className="mb-2 flex">
                  <span className="w-32 font-semibold">7-9 months:</span> 
                  <span>Review timeline from submission to award</span>
                </li>
                <li className="flex">
                  <span className="w-32 font-semibold">Up to 5 years:</span> 
                  <span>Total award duration (K99: 1-2 years; R00: 3 years)</span>
                </li>
              </ul>
            </div>
          </div>
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Application Strategy</h3>
            <BulletPoint>Develop proposal in first 3-6 months at NeuroAI Center</BulletPoint>
            <BulletPoint>Leverage center's unique datasets and computational resources</BulletPoint>
            <BulletPoint>Incorporate mentorship from both Dr. Rosenthal and Dr. Zabihi</BulletPoint>
            <BulletPoint>Include preliminary results from initial projects at the center</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Success Metrics Slide */}
      <Slide title="Expected Outcomes">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Research Deliverables</h3>
            <BulletPoint>Novel transformer architecture for multimodal neural data</BulletPoint>
            <BulletPoint>Clinical validation of prognostic models</BulletPoint>
            <BulletPoint>Open-source software and datasets</BulletPoint>
            <BulletPoint>3-4 high-impact publications</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-blue-700 mb-3">Career Advancement</h3>
            <BulletPoint>Transition to independent investigator position</BulletPoint>
            <BulletPoint>Establish independent NeuroAI research program</BulletPoint>
            <BulletPoint>Development of clinical collaborations</BulletPoint>
            <BulletPoint>Foundation for future R01 applications</BulletPoint>
          </div>
        </div>
      </Slide>
    </div>
  );
};

export default K99R00Slides;