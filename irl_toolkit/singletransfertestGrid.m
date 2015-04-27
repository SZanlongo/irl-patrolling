% Convenience script for running a single test.
addpaths;
test_result = runtransfertest( test_result.irl_result, 'mmpboost', 'linearmdp',...
    'gridworld',struct('n',50,'b',5,'determinism',0.8,'discount',0.9),...
    struct('training_sample_lengths',127,'training_samples',1,'verbosity',2));
 
% Visualize solution.
printresult(test_result);
visualize(test_result);
