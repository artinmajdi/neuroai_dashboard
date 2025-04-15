import React from 'react';

const SlideTitle = ({ children }) => (
  <div className="bg-gradient-to-r from-green-800 to-green-600 text-white p-6 rounded-t-lg">
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
    <div className="text-green-600 font-bold mr-2 mt-1">•</div>
    <div>{children}</div>
  </div>
);

const NSFCareerSlides = () => {
  return (
    <div className="w-full max-w-4xl mx-auto">
      {/* Title Slide */}
      <div className="bg-gradient-to-r from-green-900 to-green-600 text-white p-8 rounded-lg shadow-lg mb-8 text-center">
        <h1 className="text-3xl font-bold mb-4">NSF CAREER Award</h1>
        <h2 className="text-xl mb-6">Advancing NeuroAI through Integrated Research and Education</h2>
        <p className="italic">A Five-Year Research and Education Plan</p>
        <div className="mt-6 text-sm opacity-80">
          Prepared for: Mass General Brigham NeuroAI Center Interview
        </div>
      </div>

      {/* Overview Slide */}
      <Slide title="Program Overview">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Award Description</h3>
            <BulletPoint>NSF's most prestigious award for early-career faculty</BulletPoint>
            <BulletPoint>Supports those with potential to serve as academic role models</BulletPoint>
            <BulletPoint>Integrates research and education activities</BulletPoint>
            <BulletPoint>Builds foundation for lifetime of leadership</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Award Details</h3>
            <BulletPoint>5-year project period</BulletPoint>
            <BulletPoint>Minimum award of $400,000 total</BulletPoint>
            <BulletPoint>Cognitive Neuroscience program average: $175,000-$225,000 per year</BulletPoint>
            <BulletPoint>Annual submission deadline in July</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Eligibility Slide */}
      <Slide title="Eligibility & Requirements">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Eligibility Criteria</h3>
            <BulletPoint>Tenure-track (or equivalent) Assistant Professor</BulletPoint>
            <BulletPoint>Untenured at time of application</BulletPoint>
            <BulletPoint>Educational activities must be integrated with research</BulletPoint>
            <BulletPoint>Need departmental support letter</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Proposal Components</h3>
            <BulletPoint>Innovative research plan</BulletPoint>
            <BulletPoint>Integrated education plan (not just a list of activities)</BulletPoint>
            <BulletPoint>Departmental letter confirming support</BulletPoint>
            <BulletPoint>Prior NSF research results (if applicable)</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Research Plan Slide */}
      <Slide title="Proposed Research Plan">
        <h3 className="text-lg font-bold text-green-700 mb-3">NeuroAI-Based Self-Supervised Learning for Neurological Prognostication</h3>
        <div className="grid grid-cols-1 gap-4">
          <BulletPoint>
            <span className="font-semibold">Research Goal:</span> Develop novel self-supervised learning approaches for neurophysiological data that require minimal labeled examples while maintaining clinical interpretability.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Approach:</span> Implement contrastive learning techniques on unlabeled EEG and physiological data, creating foundation models that can be fine-tuned for specific clinical applications.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Technical Innovation:</span> Design neurophysiology-specific data augmentation techniques that preserve clinically relevant signal characteristics while creating diverse training examples.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Clinical Applications:</span> Apply these techniques to develop prognostic models for neurological recovery with a focus on interpretable predictions that can guide clinical decision-making.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Broader Impact:</span> Address the persistent challenge of limited labeled data in clinical neuroscience while making AI systems more accessible to non-AI specialists.
          </BulletPoint>
        </div>
      </Slide>

      {/* Education Plan Slide */}
      <Slide title="Integrated Education Plan">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Educational Goals</h3>
            <BulletPoint>Bridge the gap between neuroscience and AI education</BulletPoint>
            <BulletPoint>Increase diversity in NeuroAI workforce</BulletPoint>
            <BulletPoint>Develop interdisciplinary curriculum materials</BulletPoint>
            <BulletPoint>Engage clinicians in AI literacy</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Key Activities</h3>
            <BulletPoint>Develop "NeuroAI Bootcamp" for underrepresented students</BulletPoint>
            <BulletPoint>Create open educational resources for clinician AI literacy</BulletPoint>
            <BulletPoint>Establish mentored research program for first-gen college students</BulletPoint>
            <BulletPoint>Develop K-12 outreach program with brain-computer interface demos</BulletPoint>
          </div>
        </div>
      </Slide>

      {/* Alignment Slide */}
      <Slide title="Alignment with NeuroAI Center">
        <h3 className="text-lg font-bold text-green-700 mb-3">Strategic Alignment</h3>
        <div className="grid grid-cols-1 gap-4">
          <BulletPoint>
            <span className="font-semibold">Research Focus:</span> Self-supervised learning for neurophysiological data directly complements Dr. Zabihi's work on multimodal data integration while extending the center's capabilities to handle limited labeled data scenarios.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Clinical Translation:</span> Interpretability focus aligns with Dr. Rosenthal's emphasis on clinically relevant biomarker development and deployment of AI in neurological care.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">Educational Synergy:</span> NeuroAI Bootcamp can leverage the center's expertise and infrastructure, potentially becoming an annual program that enhances the center's educational mission.
          </BulletPoint>
          <BulletPoint>
            <span className="font-semibold">External Visibility:</span> NSF CAREER award would enhance the center's national profile in AI education and bring additional resources for educational initiatives.
          </BulletPoint>
        </div>
      </Slide>

      {/* Timeline Slide */}
      <Slide title="Timeline & Implementation">
        <div className="mb-4">
          <h3 className="text-lg font-bold text-green-700 mb-3">5-Year Research & Education Roadmap</h3>
          <div className="bg-green-50 p-4 rounded-lg">
            <ul className="list-none">
              <li className="mb-3 flex">
                <span className="w-24 font-semibold">Year 1:</span> 
                <span>Develop foundational self-supervised learning framework; launch pilot NeuroAI Bootcamp</span>
              </li>
              <li className="mb-3 flex">
                <span className="w-24 font-semibold">Year 2:</span> 
                <span>Extend framework to multimodal data; create open educational resources</span>
              </li>
              <li className="mb-3 flex">
                <span className="w-24 font-semibold">Year 3:</span> 
                <span>Implement clinical validation; expand mentored research program</span>
              </li>
              <li className="mb-3 flex">
                <span className="w-24 font-semibold">Year 4:</span> 
                <span>Develop interpretability tools; establish K-12 outreach program</span>
              </li>
              <li className="flex">
                <span className="w-24 font-semibold">Year 5:</span> 
                <span>Deploy integrated system in clinical environment; assess educational outcomes</span>
              </li>
            </ul>
          </div>
        </div>
        <div>
          <h3 className="text-lg font-bold text-green-700 mb-3">Application Strategy</h3>
          <BulletPoint>Submit proposal after first year at NeuroAI Center (July 2026)</BulletPoint>
          <BulletPoint>Obtain preliminary data through initial center projects</BulletPoint>
          <BulletPoint>Secure departmental and institutional support letters</BulletPoint>
          <BulletPoint>Develop education plan in collaboration with Harvard and MGH educational offices</BulletPoint>
        </div>
      </Slide>

      {/* Expected Outcomes Slide */}
      <Slide title="Expected Outcomes & Impact">
        <div className="grid grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Research Outcomes</h3>
            <BulletPoint>Novel self-supervised learning framework for clinical neuroscience</BulletPoint>
            <BulletPoint>Reduction in labeled data requirements by 60-70%</BulletPoint>
            <BulletPoint>Open-source software library and benchmark datasets</BulletPoint>
            <BulletPoint>5+ peer-reviewed publications in top AI and neuroscience journals</BulletPoint>
          </div>
          <div>
            <h3 className="text-lg font-bold text-green-700 mb-3">Educational Impact</h3>
            <BulletPoint>Train 50+ students from underrepresented backgrounds in NeuroAI</BulletPoint>
            <BulletPoint>Develop curriculum used by 10+ institutions</BulletPoint>
            <BulletPoint>Increase AI literacy among 100+ clinicians</BulletPoint>
            <BulletPoint>Establish sustainable educational programs that continue beyond award period</BulletPoint>
          </div>
        </div>
      </Slide>
    </div>
  );
};

export default NSFCareerSlides;