% Convenience script for running a single test.
addpaths;
test_result = runtest('an',struct(),'linearmdp',...
    'objectworld',struct('n',50,'determinism',1,'seed',1,'continuous',0),...
    struct('training_sample_lengths',127,'training_samples',1,'verbosity',2));
 
% Visualize solution.
printresult(test_result);
visualize(test_result);
