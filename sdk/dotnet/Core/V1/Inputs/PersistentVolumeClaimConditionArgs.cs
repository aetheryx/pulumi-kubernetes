// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Inputs.Core.V1
{

    /// <summary>
    /// PersistentVolumeClaimCondition contails details about state of pvc
    /// </summary>
    public class PersistentVolumeClaimConditionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// lastProbeTime is the time we probed the condition.
        /// </summary>
        [Input("lastProbeTime")]
        public Input<string>? LastProbeTime { get; set; }

        /// <summary>
        /// lastTransitionTime is the time the condition transitioned from one status to another.
        /// </summary>
        [Input("lastTransitionTime")]
        public Input<string>? LastTransitionTime { get; set; }

        /// <summary>
        /// message is the human-readable message indicating details about last transition.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports "ResizeStarted" that means the underlying persistent volume is being resized.
        /// </summary>
        [Input("reason")]
        public Input<string>? Reason { get; set; }

        [Input("status", required: true)]
        public Input<string> Status { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public PersistentVolumeClaimConditionArgs()
        {
        }
    }
}
