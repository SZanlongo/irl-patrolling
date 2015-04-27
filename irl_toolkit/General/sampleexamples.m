% Sample example tranjectories from the state space of a given MDP.
function example_samples = sampleexamples(mdp_model,mdp_data,mdp_solution,test_params)

% Allocate training samples.
N = test_params.training_samples;
T = test_params.training_sample_lengths;
example_samples = cell(N,T);

% Sample trajectories.
fid(1) = fopen('t1.txt');
fid(2) = fopen('t2.txt');
fid(3) = fopen('t3.txt');
fid(4) = fopen('t4.txt');
fid(5) = fopen('t5.txt');
fid(6) = fopen('t6.txt');
fid(7) = fopen('t7.txt');
fid(8) = fopen('t8.txt');
fid(9) = fopen('t9.txt');
fid(10) = fopen('t10.txt');
s=zeros(1);
for i=1:N,
    % Sample initial state.
     %s = ceil(rand(1,1)*mdp_data.states);
    as = fgetl(fid(i));
    %s=as;
    s=as(1,1);
    %size(s)
    %s
    % Run sample trajectory.
    for t=1:T,
        % Compute optimal action for current state.
        a = feval(strcat(mdp_model,'action'),mdp_data,mdp_solution,s);
        %size(a)
        % Store example.
        example_samples{i,t} = [s;a];
        
        % Move on to next state.
        % s = feval(strcat(mdp_model,'step'),mdp_data,mdp_solution,s,a);
        if(t==1)
            continue
        else
        s = fgetl(fid(i));
        end
        
       % s=as(1,1);
        s = feval(strcat(mdp_model,'step'),mdp_data,mdp_solution,s,a);
        
    end;
    i
end;
