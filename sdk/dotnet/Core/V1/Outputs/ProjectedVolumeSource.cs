// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Core.V1
{

    /// <summary>
    /// Represents a projected volume source
    /// </summary>
    [OutputType]
    public sealed class ProjectedVolumeSource
    {
        /// <summary>
        /// defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.
        /// </summary>
        public readonly int DefaultMode;
        /// <summary>
        /// sources is the list of volume projections
        /// </summary>
        public readonly ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.VolumeProjection> Sources;

        [OutputConstructor]
        private ProjectedVolumeSource(
            int defaultMode,

            ImmutableArray<Pulumi.Kubernetes.Types.Outputs.Core.V1.VolumeProjection> sources)
        {
            DefaultMode = defaultMode;
            Sources = sources;
        }
    }
}
